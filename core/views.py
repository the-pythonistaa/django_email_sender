from django.shortcuts import render,reverse, render_to_response, redirect
from django.http import HttpResponseRedirect

from smtplib import SMTP
from email.mime.text import MIMEText

from .forms import EmailListForm
from mailer import settings

from os import path
from datetime import datetime


def content_setter(sending_to, file_name):
    email_temaplate = open(file_name, 'r+')
    message = email_temaplate.read()
    my_email = MIMEText(message, "html")
    my_email["Subject"] = "Hello!"

    send_to = sending_to

    email_server = SMTP(settings.EMAIL_SMTP_SERVER, settings.EMAIL_SERVER_PORT)
    email_server.starttls()
    email_server.login(settings.SENDER_EMAIL, settings.SENDER_EMAIL_PASSWORD)
    email_server.sendmail(settings.SENDER_EMAIL, send_to, my_email.as_string())

    return my_email


def handle_uploaded_file(f):

    file_name = path.join(settings.MEDIA_ROOT, f'{int(datetime.now().timestamp())}.html')
    #file will be uploaded to media directory
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    return file_name


def send(request):
    try :
        file = request.FILES['html_file']
        file_name = handle_uploaded_file(file)
        email_list = request.POST['email_list'].split(',')
        final_email = {}

        for email in email_list:
            try:
                content_setter(email, file_name)
                final_email[email] = "Sent"
            except Exception as e:
                if settings.DEBUG:
                    final_email[email] = f"Error: {e}"
                else:
                    final_email[email] = f"Error: Something went wrong while sending email"
        return render_to_response("core/layout.html", {"final_email": final_email, "form": EmailListForm()})
    except KeyError:
        return HttpResponseRedirect(reverse('core:index'))


def index(request):
    return render(request, 'core/layout.html', {"form": EmailListForm()})
