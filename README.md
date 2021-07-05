# BUILDING AN ECOMMERCE APPLICATION USING DJANGO 
This is my exercise based on the tutorials made by Yuksel CELIK, PhD on Youtube

### Links to sources:

https://github.com/gurnitha/django-russian-ecommerce
https://www.youtube.com/watch?v=6RR8WrvshQA&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk&index=2


### ----------
### 1. SETUP
### ----------


#### 1.1.1 Create remote repository Github

        modified:   .gitignore
        modified:   README.md

#### 1.2.2 Other requirements 

        NOTE: 
        Other requirements, such as Python, Virtualenv have been installed.
        So, local environmente is ready to develop the project

        modified:   README.md

#### 1.3.3 Create virtualenv

        λ python -m venv venv3932

        modified:   README.md

#### 1.4.4 Install Django

        λ venv3932\scripts\activate
        (venv3932) λ python -m pip install django
        Successfully installed asgiref-3.4.1 django-3.2.5 pytz-2021.1 sqlparse-0.4.1
        (venv3932) λ python -m pip install --upgrade pip

        modified:   README.md



### --------------------
### 2. PROJECT AND APP
### --------------------


#### 2.1.5 Create project 'config'

        (venv3932) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 2.2.6 Create app 'apps/home'

        (venv3932) λ mkdir apps
        (venv3932) λ mkdir apps\home
        (venv3932) λ python manage.py startapp home apps/home

        modified:   README.md
        new file:   apps/home/__init__.py
        new file:   apps/home/admin.py
        new file:   apps/home/apps.py
        new file:   apps/home/migrations/__init__.py
        new file:   apps/home/models.py
        new file:   apps/home/tests.py
        new file:   apps/home/views.py

#### 2.3.7 Install app to project

        modified:   README.md
        modified:   apps/home/apps.py
        modified:   config/settings.py

        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced). 

#### 2.4.8 Current project's structure

        .
        ├── LICENSE
        ├── README.md
        ├── apps
        │   └── home
        │       ├── __init__.py
        │       ├── __pycache__
        │       ├── admin.py
        │       ├── apps.py
        │       ├── migrations
        │       ├── models.py
        │       ├── tests.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-39.pyc
        │   │   ├── settings.cpython-39.pyc
        │   │   └── urls.cpython-39.pyc
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── manage.py
        └── venv3932

        modified:   README.md


### --------------
### 3. DATABASE
### --------------

#### 3.1.9 Create postgres database

        hp=# CREATE DATABASE django_russian_ecommerce;
        CREATE DATABASE
        hp=#

        modified:   .gitignore
        modified:   README.md



















































































































































