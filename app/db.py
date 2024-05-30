import psycopg2
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

logging.info(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")


if os.getenv('FLASK_ENV') == 'prod':
    load_dotenv('.env.prod')
elif os.getenv('FLASK_ENV') == 'qa':
    load_dotenv('.env.qa')
else:
    load_dotenv('.env.dev') 

def db_connection():
    try:
        conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None    