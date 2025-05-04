from flask import Flask, render_template, request, jsonify, url_for
from flask_mail import Mail, Message
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, 
    static_folder='static', 
    template_folder='templates'  
)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD') 
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')  
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

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

        # Log form submission
        logger.info(f"Received contact form submission from {name} ({email})")

        # Validate required fields
        if not all([name, email, phone, service, message]):
            logger.warning("Missing required fields in contact form")
            return jsonify({
                'status': 'error',
                'message': 'All fields are required'
            }), 400

        # Create email message for admin (sent to receiver email)
        admin_msg = Message(
            subject=f'New Contact Form Submission - {service}',
            sender=app.config['MAIL_USERNAME'], 
            recipients=[RECEIVER_EMAIL], 
            reply_to=email  

        admin_msg.body = f"""
        New Contact Form Submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Service: {service}
        Message: {message}
        """

        logger.info(f"Sending admin notification email to {RECEIVER_EMAIL}")
        mail.send(admin_msg)

        user_msg = Message(
            subject='Thank you for contacting NexGen Developers',
            sender=app.config['MAIL_USERNAME'],  # Sender email
            recipients=[email]  # Form submitter's email
        )
        
        user_msg.body = f"""
        Dear {name},

        Thank you for contacting NexGen Developers. We have received your message and will get back to you shortly.

        Best regards,
        NexGen Developers Team
        """

        logger.info(f"Sending confirmation email to {email}")
        mail.send(user_msg)

        logger.info("Contact form submission processed successfully")
        return jsonify({
            'status': 'success',
            'message': 'Your message has been sent successfully!'
        })

    except Exception as e:
        logger.error(f"Error in contact form: {str(e)}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while sending your message. Please try again later.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)

app = app
