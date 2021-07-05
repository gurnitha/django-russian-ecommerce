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

#### 3.2.10 Install django environ

       (venv3932) λ pip install django-environ

       modified:   README.md

#### 3.3.11 Install PostgreSQL driver

       (venv3932) λ python -m pip install psycopg2-binary==2.8.6

       modified:   README.md 

#### 3.4.12 Create .env file and setup environ

       (venv3932) λ touch config\.env

        modified:   README.md

#### 3.5.13 Use environ in settings

       (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py


### ----------------
### 4. TEMPLATING
### ----------------


#### 4.1.14 Template, View, Url - Hellow World

        modified:   README.md
        new file:   apps/home/templates/home/index.html
        new file:   apps/home/urls.py
        modified:   apps/home/views.py
        modified:   config/urls.py

#### 4.2.15 Adding html template to homepage and static files

        modified:   README.md
        new file:   apps/home/static/css/bootstrap.min.css
        ...
        modified:   apps/home/templates/home/index.html

#### 4.3.16 Loading static files

        modified:   README.md
        modified:   apps/home/templates/home/index.html 

#### 4.4.17 Create a new folder 'templates' and base.html file

        modified:   README.md
        new file:   templates/base.html

#### 4.5.18 Activating template engine

        modified:   README.md
        modified:   config/settings.py 

#### 4.6.19 Using template inheritance

        modified:   README.md
        modified:   apps/home/templates/home/index.html
        modified:   templates/base.html 

#### 4.7.20 Defining MEDIA_URL and MEDIA_ROOT

        modified:   README.md
        modified:   config/settings.py


### ----------------------------
### 5. WORKING ON PRODUCT APP
### ----------------------------


#### 5.1.21 Creating a new app 'apps/product'

        (venv3932) λ mkdir apps\product
        (venv3932) λ python manage.py startapp product apps/product

#### 5.2.22 Install the product app to project 

        (venv3932) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   apps/product/apps.py
        modified:   config/settings.py

#### 5.3.23 Create Category model with MPTT

        (venv3932) λ pip install django-mptt 
        (venv3932) λ python -m pip install Pillow

        modified:   README.md
        new file:   apps/product/migrations/0001_initial.py
        modified:   apps/product/models.py
        modified:   config/settings.py

        """
        What is Modified Preorder Tree Traversal?

        MPTT is a technique for storing hierarchical data in a database. The aim is to make retrieval operations very efficient.

        The trade-off for this efficiency is that performing inserts and moving items around the tree is more involved, as there’s some extra work required to keep the tree structure in a good state at all times.

        Links:

        Source:
        https://django-mptt.readthedocs.io/en/latest/overview.html
        
        Articles about MPTT:

        https://www.ibase.ru/files/articles/programming/dbmstrees/sqltrees.html
        https://www.sitepoint.com/hierarchical-data-database/
        http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/
        """

#### 5.4.24 Admin - Register Category model to admin 

        modified:   README.md
        modified:   apps/product/admin.py

#### 5.5.25 Admin - Create superuser

        (venv3932) λ python manage.py createsuperuser


#### 5.6.26 Defining MEDIA_URL and MEDIA_ROOT

        --> see :4.7.20 Defining MEDIA_URL and MEDIA_ROOT

        modified:   README.md
        modified:   config/urls.py
        new file:   uploads/images/vandi-patns-c.PNG

        NOTE:

        To define MEDIA_URL and MEDIA_ROOT, do at once:
        steps: 4.7.20 and 5.6.26

#### 5.7.27 Adding categories and images as parent categoy

        modified:   README.md
        new file:   uploads/images/elecktronics.png
        new file:   uploads/images/nike-tshirt.png

#### 5.8.28 Adding child categories

        modified:   README.md
        new file:   uploads/images/banner04.jpg
        new file:   uploads/images/men-suit.PNG
        new file:   uploads/images/samsung-tv.PNG

#### 5.9.29 Create Product models with OneToMany Relationship with Category and run migration

        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).
        (venv3932) λ python manage.py makemigrations
        (venv3932) λ python manage.py migrate

        modified:   README.md
        new file:   apps/product/migrations/0002_product.py
        modified:   apps/product/models.py

#### 5.10.30 Register Product model to admin and insert some items to Product model

        modified:   README.md
        modified:   apps/product/admin.py
        new file:   uploads/images/samsung-tv-tu685.PNG
        new file:   uploads/images/samsung-tv-ua65t.PNG
        new file:   uploads/images/women-casual-lady-shoe.PNG
        new file:   uploads/images/women-casual-lady-short-lenin-blue.PNG 


#### 5.11.31 Showing image thumbnail in Admin dashboard

        modified:   README.md
        modified:   apps/product/admin.py
        modified:   apps/product/models.py 




















































































