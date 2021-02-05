#!/usr/bin/env python3
# STD
import logging

# PIP
import psycopg2

# LOCAL

_log = logging.getLogger(__name__)


def connect_db_with_config(config: dict):
    psql_config = config["psql"]
    host = psql_config["host"]
    port = psql_config["port"]
    user = psql_config["username"]
    password = psql_config["password"]
    database = psql_config["database"]
    return connect_to_db(host, port, user, password, database)


def connect_to_db(host: str, port: int, user: str, password: str, database: str):
    conn = psycopg2.connect(
        host=host, port=port, user=user, password=password, dbname=database
    )
    return conn


def main():
    conn = connect_to_db("164.111.161.173", 5432, "team5", "5team5", "team5")
    print(conn)


if __name__ == "__main__":
    main()
