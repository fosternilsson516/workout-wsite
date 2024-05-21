import psycopg2
import os
from dotenv import load_dotenv


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