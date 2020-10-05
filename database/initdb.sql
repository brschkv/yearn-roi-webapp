CREATE DATABASE IF NOT EXISTS yearn DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_bin;

CREATE USER webapp@localhost IDENTIFIED BY RANDOM PASSWORD;
CREATE USER model@localhost IDENTIFIED BY RANDOM PASSWORD;
GRANT ALL PRIVILEGES ON yearn.* TO model@localhost;
GRANT SELECT ON yearn.* TO webapp@localhost;
FLUSH PRIVILEGES;

USE yearn;

CREATE TABLE IF NOT EXISTS vaults
(
    name                    varchar(64),
    smart_contract_address  varchar(64),
    first_block_with_price  int,
    decimals                int,
    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS blocks
(
    number      bigint,
    timestamp   TIMESTAMP,
    PRIMARY KEY (number),
    INDEX (number)
);

CREATE TABLE IF NOT EXISTS historic_prices
(
    block   int,
    price   bigint,
    vault   varchar(64),
    PRIMARY KEY (block, vault),
    INDEX (block, vault)
);

CREATE TABLE IF NOT EXISTS models
(
    timestamp       timestamp,
    hpd_95_lower    double,
    hpd_95_upper    double,
    hpd_50_lower    double,
    hpd_50_upper    double,
    vault           varchar(64),
    base_days       int,
    PRIMARY KEY (timestamp, vault, base_days),
    INDEX (vault, base_days)
);
