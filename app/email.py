from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

#poczytać jeszcze o tym dlaczego app jako argument daje

#Flask uses contexts to avoid having to pass arguments across functions.

#there are two types of contexts, the application context and the request context. In most cases, these contexts are automatically managed by the framework, but when the application starts custom threads, contexts for those threads may need to be manually created.

#The reason many extensions need to know the application instance is because they have their configuration stored in the app.config object

#The mail.send() method needs to access the configuration values for the email server, and that can only be done by knowing what the application is. 

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()