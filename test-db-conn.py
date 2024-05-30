import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
if os.getenv('FLASK_ENV') == 'prod':
    load_dotenv('.env.prod')
elif os.getenv('FLASK_ENV') == 'qa':
    load_dotenv('.env.qa')
else:
    load_dotenv('.env.dev')

print("DB_NAME:", os.getenv('DB_NAME'))
print("DB_USER:", os.getenv('DB_USER'))
print("HOST:", os.getenv('HOST'))
print("PORT:", os.getenv('PORT'))    

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    print("Database connection established successfully.")
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
