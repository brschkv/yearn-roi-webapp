FROM python:3.8-buster

RUN adduser --system --group api
WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

ARG FLASK_ENV=production

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:API", "-w4"]
