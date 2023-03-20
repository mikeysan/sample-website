from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import os

from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure CSRF protection
csrf = CSRFProtect(app)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'
mail = Mail(app)

# Configure upload settings
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the gallery page
@app.route('/gallery')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Send email
        msg = Message(subject=form.subject.data,
                      recipients=['your_email@example.com'],
                      body=form.message.data,
                      sender=form.email.data)
        mail.send(msg)
        flash('Your message has been sent.')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

# Route for handling file uploads
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Your file has been uploaded.')
    else:
        flash('Invalid file type.')
    return redirect(url_for('gallery'))

# Function for checking allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

if __name__ == '__main__':
    app.run(debug=True)
