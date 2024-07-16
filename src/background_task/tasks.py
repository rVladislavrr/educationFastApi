import smtplib
from email.message import EmailMessage
from celery import Celery
from config import settings

celery = Celery('background_task', broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}')

password_m = settings.PASS
mail_ = settings.MAIL

def get_email(username, mail):
    email = EmailMessage()
    email['From'] = mail_
    email['To'] = mail
    email['Subject'] = username
    email.set_content(
        f'<h1>Hello {username}</h1>',
        subtype='html',
    )
    return email


@celery.task
def send_email(username, mail):
    email = get_email(username, mail)
    with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:
        server.login(mail_, password_m)
        server.send_message(email)
