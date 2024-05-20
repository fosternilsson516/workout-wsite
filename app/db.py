from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


load_dotenv('.env.prod') 

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

from sqlalchemy import text

def store_answers(data):
    insert_query = text(
        "INSERT INTO responses (email, answers) VALUES (:email, :answers)"
    )

    with engine.connect() as connection:
        connection.execute(insert_query, email=data['Email'], answers=str(data))