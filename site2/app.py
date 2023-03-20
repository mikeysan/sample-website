from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Add your models here
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    img_path = db.Column(db.String(200), nullable=False)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])

@app.route('/')
def home():
    photos = Photo.query.all()
    return render_template('home.html', photos=photos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Send email using Flask-Mail
        mail = Mail(app)
        msg = Message('Message from your portfolio website', sender=email, recipients=['youremail@example.com'])
        msg.body = f'From: {name}\nEmail: {email}\n\n{message}'
        mail.send(msg)

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route('/gallery')
def gallery():
    photos = Photo.query.all()
    return render_template('gallery.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
