# Django - UWEFlix
A Django system for the online purchasing of cinema tickets - Coursework for Enterprise Systems Development final year module.


Libraries included:
- django
- virtualenv
- pillow
- mysql
- pymysql
- mysqlclient
- django-environ
- django_credit_cards
- django-bootstrap4


Activating virtual environment:
- py -m virtualenv venv
- . .\venv\scripts\activate


Connecting to database: (SQL)
- Create a new empty db called uwe-flix
- py manage.py migrate  


Start server:
- py manage.py runserver

Create an admin account:
- py manage.py createsuperuser -> add username, email and password
