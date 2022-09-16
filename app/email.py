from flask_mail import Message
from app import mail
from flask import render_template
from app import app
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

#poczytać jeszcze o tym dlaczego app jako argument daje

#Flask uses contexts to avoid having to pass arguments across functions.

#there are two types of contexts, the application context and the request context. In most cases, these contexts are automatically managed by the framework, but when the application starts custom threads, contexts for those threads may need to be manually created.

#The reason many extensions need to know the application instance is because they have their configuration stored in the app.config object

#The mail.send() method needs to access the configuration values for the email server, and that can only be done by knowing what the application is. 

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))