from flask import Blueprint, render_template

# Create a Blueprint
main_page_bp = Blueprint('main_page_bp', __name__)

@main_page_bp.route('/')
def home():
    return render_template('home.html')
