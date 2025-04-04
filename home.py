from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'anitjohnsaji41@gmail.com'
app.config['MAIL_PASSWORD'] = 'vogl rwus lgcz memq'
app.config['MAIL_USE_TLS'] = True  # Changed from False to True
app.config['MAIL_USE_SSL'] = False  # Changed from True to False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])  # Changed from '/send_mail' to '/submit' to match form action
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = Message(
        subject=f'Portfolio Contact from {name}',  # More descriptive subject
        sender=app.config['MAIL_USERNAME'],  # Use your email as sender
        reply_to=email,  # Set reply-to as the contact's email
        recipients=[app.config['MAIL_USERNAME']]  # Send to yourself
    )
    msg.body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    try:
        mail.send(msg)
        return render_template('index.html', success=True)
    except Exception as e:
        print(f"Error sending email: {e}")
        return render_template('index.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)