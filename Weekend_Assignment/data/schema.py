import sqlite3
import os

"""
pk INTEGER
Name VARCHAR
Yr_release INTEGER
Version_number INTEGER
Creator VARCHAR
OP INTEGER  #OriginalPrice
CP INTEGER  #CurrentPrice
Company VARCHAR
Contact_number INTEGER
Contact_email VARCHAR
"""

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "listings.db")
print(DATAPATH)

def schema(dbpath=DATAPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS listings(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR,
                Yr_release INTEGER,
                Version_number INTEGER,
                Creator VARCHAR,
                OP INTEGER,
                CP INTEGER,
                Company VARCHAR,
                Contact_number INTEGER,
                Contact_email VARCHAR
        );"""

        cursor.execute(sql)

if __name__ == "__main__":
    schema()