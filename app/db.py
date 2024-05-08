from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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