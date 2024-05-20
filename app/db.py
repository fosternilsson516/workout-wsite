from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
import os
from dotenv import load_dotenv

load_dotenv('.env.prod') 

DATABASE_URL = os.getenv('DATABASE_URL')

# Explicitly create engine with PyMySQL dialect
engine = create_engine(DATABASE_URL, connect_args={'ssl_ca':"/etc/ssl/certs/ca-certificates.crt"})
db = SQLAlchemy(app)

Session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

class Response(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    answers = db.Column(db.Text, nullable=False)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all() 

def store_answers(data):
    new_response = Response(email=data['Email'], answers=str(data))
    db.session.add(new_response)
    db.session.commit()