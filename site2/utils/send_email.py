from flask import current_app
from flask_mail import Message
from threading import Thread
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to])
    msg.html = template
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
