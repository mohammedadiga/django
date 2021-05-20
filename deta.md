1-cryat new venv:
    -py -m venv env

2-connect venv:
    -cd venv-\
    -Scripts\activate

3-upload project on githup

4-install django
    -pip install django

5-ceryate django project
    -django-admin startproject project .

6-cehek server is run
    -python manage.py runserver

7-extract all backgec for requirements.txt
    -pip freeze > requirements.txt

8-ceryate django app
    -python manage.py startapp {appname/blog}