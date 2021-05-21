- frontend template
- virtualenv :
    -Create ==> py -m venv env 
    -activate  ==>  1-cd venv-\
                    2-Scripts\activate
    -install django  ==>  pip install django

    -Start New Project ==> django-admin startproject project .

    -Start All App ==> 
        [python manage.py startapp {appname/blog}]
        [python manage.py startapp {appname/job}]
        [python manage.py startapp {appname/accounts}]
        [python manage.py startapp {appname/contact}]
        [python manage.py startapp {appname/home}] 
    -deactivate 

    
    -Bush All data in DATABASES --DATABASES_FILI is['db.sqlite3']-- ==> [python manage.py migrate]
    -Create User And Password For login in DATABASES ==> [python manage.py createsuperuser]

    -chek app ==> [python manage.py makemigrations]  --> So Bush the DATABASES in ==> [python manage.py migrate]
    -run server in locallhost ==>  [python manage.py runserver]


    -extract all packages for requirements.txt ==> [pip freeze > requirements.txt]

- Upload Project On GitHub

- URL : path
- View : logic
- models : db
- templates : frontend