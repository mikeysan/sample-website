from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        msg = Message(subject, sender=email, recipients=['youremail@gmail.com'])
        msg.body = f"From: {name}\nEmail: {email}\n\n{message}"
        mail.send(msg)
        return redirect(url_for('contact_success'))
    return render_template('contact.html', form=form)

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

if __name__ == '__main__':
    app.run(debug=True)
