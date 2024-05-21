from app.db import db_connection
import psycopg2

class UserQuestions:
    def __init__(self):
        self.conn = db_connection()

    def set_answers(self, data):
        if self.conn is None or self.conn.closed:
            self.conn = db_connection()
        try:
            cursor = self.conn.cursor()

            cursor.execute("INSERT INTO responses (data) VALUES (%s)",
                            (data,))
            self.conn.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Error executing SQL query:", e)
        finally:
            if self.conn:
                self.conn.close()     