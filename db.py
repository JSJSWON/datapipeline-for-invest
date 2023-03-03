import psycopg2
import json
import time
from price import *

price = Price()

db_secrets_path = "db_secret.json"
with open(db_secrets_path, "r") as f:
    db_secrets = json.load(f)


def write_price(currency_name):
    db = psycopg2.connect(host=db_secrets["host"], dbname=db_secrets["dbname"],
                          user=db_secrets["user"], port=db_secrets["port"])

    # while True:
    for _ in range(100):
        info = price("BTC")
        db.cursor().execute(
            f"""
            insert into price (currency_name, opening_price, closing_price, min_price, 
                                max_price, units_traded, acc_trade_value, prev_closing_price, 
                                "units_traded_24H", "acc_trade_value_24H", "fluctate_24H", "fluctate_rate_24H")
             values (\'{currency_name}\', {int(info['opening_price'])}, {int(info['closing_price'])}, 
                        {int(info['min_price'])}, {int(info['max_price'])}, {float(info['units_traded'])}, 
                        {float(info['acc_trade_value'])}, {int(info['prev_closing_price'])}, {float(info['units_traded_24H'])}, 
                        {float(info['acc_trade_value_24H'])}, {int(info['fluctate_24H'])}, {float(info['fluctate_rate_24H'])})
            """
        )
        db.commit()
        time.sleep(1)

    db.close()
