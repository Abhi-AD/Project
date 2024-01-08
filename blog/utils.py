import time
from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
     subject ='Django'
     message ='This is client text the server!'
     from_email= settings.EMAIL_HOST_USER
     recipient_list = ['dangiabhi332@gmail.com']
     send_mail(subject, message, from_email, recipient_list)