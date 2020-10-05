import os
from typing import List, Dict

from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


API = Flask(__name__)
API.config['SQLALCHEMY_DATABASE_URI'] = f"{os.environ['DB_PROTOCOL']}://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_DATABASE']}"
db = SQLAlchemy(API)


def to_float(mantissa: int, scale_factor: int = 1e18) -> float:
    if type(mantissa) is str:
        mantissa = int(mantissa)
    return mantissa / scale_factor


def create_response(data) -> Response:
    response = jsonify(data)
    response.status_code = 200
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@API.route('/api/vaults', methods=['GET'])
def get_vaults() -> Response:
    query = f"""
        SELECT
            name
        FROM
            vaults
        ;
    """
    result = db.engine.execute(query)
    vaults = [row[0] for row in result]
    response = create_response(vaults)
    return response


def extract_points(s: pd.Series) -> List[Dict]:
    points = []
    for index, value in s.iteritems():
        points.append(
            {
                'x': index.date().strftime('%Y-%m-%d'),
                'y': value
            }
        )
    return points


def get_historic_prices(vault: str) -> pd.Series:
    historic_prices_query = f"""
                SELECT
                    h.block,
                    h.price,
                    b.timestamp
                FROM
                    historic_prices h
                INNER JOIN
                    blocks b
                    ON b.number = h.block
                WHERE
                    h.vault = '{vault}'
                ;
            """
    historic_prices = pd.read_sql(historic_prices_query, db.engine, parse_dates=True)
    historic_prices = historic_prices.set_index('timestamp')
    historic_prices = historic_prices.resample('1D').nearest()
    historic_prices = historic_prices.sort_index(ascending=True)
    return historic_prices['price'].apply(to_float)


def get_model(vault: str, base_days: int) -> pd.DataFrame:
    model_query = f"""
        SELECT
            timestamp,
            hpd_95_lower,
            hpd_95_upper,
            hpd_50_lower,
            hpd_50_upper
        FROM
            models m
        WHERE
            m.vault = '{vault}'
            AND m.base_days = {base_days}
        ;
    """
    model = pd.read_sql(model_query, db.engine, parse_dates=True)
    model = model.set_index('timestamp')
    model = model.sort_index(ascending=True)
    return model


def prepend_latest_price(historic_prices: pd.Series, model: pd.DataFrame) -> pd.DataFrame:
    latest_known_date = historic_prices.index.max()
    model.loc[latest_known_date] = historic_prices.loc[latest_known_date]
    model = model.sort_index(ascending=True)
    return model


@API.route('/api/projection/<vault>/<base_days>/<horizon_days>', methods=['GET'])
def get_projection(vault: str, base_days: str, horizon_days: str) -> Response:
    base_days = int(base_days)
    horizon_days = int(horizon_days)

    data = {}

    historic_prices = get_historic_prices(vault)
    data['price'] = extract_points(historic_prices)[-base_days:]

    model = get_model(vault, base_days)
    model = prepend_latest_price(historic_prices, model)
    for c in model.columns:
        data[c] = extract_points(model[c][:horizon_days+1])

    response = create_response(data)
    return response
