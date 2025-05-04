from flask import Flask, render_template, request, jsonify, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app with explicit static folder
app = Flask(__name__,
    static_folder='static',
    static_url_path='/static'
)

# Basic configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# Initialize Mail
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')

        # Validate required fields
        if not all([name, email, phone, service, message]):
            return jsonify({
                'status': 'error',
                'message': 'All fields are required'
            }), 400

        # Create email message
        msg = Message(
            subject=f'New Contact Form Submission - {service}',
            sender=app.config['MAIL_USERNAME'],
            recipients=[os.getenv('RECEIVER_EMAIL')],
            reply_to=email
        )

        msg.body = f"""
        New Contact Form Submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Service: {service}
        Message: {message}
        """

        # Send email
        mail.send(msg)

        return jsonify({
            'status': 'success',
            'message': 'Your message has been sent successfully!'
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while sending your message. Please try again later.'
        }), 500

# For Vercel
app = app
