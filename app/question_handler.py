from app.db import db_connection
import psycopg2
import logging

class UserQuestions:
    def __init__(self):
        self.conn = db_connection()
        if self.conn is None:
            logging.error("Failed to establish database connection.")
        else:
            logging.info("Database connection established successfully.")

    def set_answers(self, json_data):
        if self.conn is None:
            logging.error("Database connection is not established.")
            raise ValueError("Database connection is not established")
        try:
            cursor = self.conn.cursor()
            logging.info("Cursor created successfully.")

            cursor.execute("INSERT INTO responses (data) VALUES (%s)",
                            (json_data,))
            self.conn.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Error executing SQL query:", e)
        finally:
            if self.conn:
                self.conn.close()     