"""this files makes a connection to mysql server db"""

import mysql.connector
from mysql.connector import Error
import config


def create_connection():
    """'connects to the banking DB"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DATABASE,
        )
    except Error as e:
        print(
            f"\n --------------- ERROR: Database Connection Failed. {e}  --------------- \n"
        )
    return connection
