from .main_page import main_page_bp
from .quiz import quiz_bp

def init_app(app):
    app.register_blueprint(main_page_bp)
    app.register_blueprint(quiz_bp)