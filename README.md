# django_email_sender

### Installation
[Python >= 3.6.x](https://www.python.org/).

[Django >= 2.2](https://docs.djangoproject.com/en/2.2/topics/install/#installing-official-release) to run this project.

### Install the dependencies and devDependencies and start the server.

```sh
$ cd django_email_sender
$ pip install -r requirements.txt
```

### Todos
 - Set your email server and ports at in settings.py 
    ``` # email server and related settings 
    EMAIL_SMTP_SERVER = 'smtp.gmail.com' 
    EMAIL_SERVER_PORT = 587
 - Set email and password
 - if you are going to use Google Account that this may be helpfull :[AppPassword](https://myaccount.google.com/apppasswords)
    ```# email credentials which needs to send email from
    SENDER_EMAIL =  "your_email_id@domain.com"
    SENDER_EMAIL_PASSWORD = "your_email_password"
```sh
$ python manage.py runserver
```
