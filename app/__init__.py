from flask import Flask
from dotenv import load_dotenv
import os
from .mail import init_mail

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    if os.getenv('FLASK_ENV') == 'prod':
        load_dotenv('.env.prod')
    elif os.getenv('FLASK_ENV') == 'qa':
        load_dotenv('.env.qa')
    else:
        load_dotenv('.env.dev')     

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    init_mail(app)

    from .routes import init_app
    init_app(app)

    return app