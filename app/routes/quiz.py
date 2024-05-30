from flask import Blueprint, render_template, request, jsonify, current_app
from ..mail import mail
from flask_mail import Message
from app.question_handler import UserQuestions
import json

quiz_bp = Blueprint('quiz_bp', __name__)
question_handler = UserQuestions()

@quiz_bp.route('/quiz')
def quiz():
    return render_template('quiz.html')

@quiz_bp.route('/submit_answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    #print(json_data_dict)
    #data = json.dumps(json_data_dict)

    question_handler.set_answers(data)

    base_message = f"Here are your answers: {data}"
    text_body = f"Hello,\n\n{base_message}\n\nThank you for participating."
    html_body = f"<p>Hello,</p><p>{base_message}</p><p>Thank you for participating.</p>"

    # Assume the email is part of the data under the key 'Email'
    email_address = data.get('Email')
    if email_address:
        # Create a new message
        msg = Message("Thank You for Your Submission!",
                      sender=current_app.config['MAIL_USERNAME'],
                      recipients=[email_address])
        msg.body = text_body
        msg.html = html_body

        # Send the message
    try:
        mail.send(msg)
        return jsonify({'status': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'status': 'Failed to send email', 'reason': str(e)})

