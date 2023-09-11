<h1 align='center'>Django custom commands to run scripts</h1>


## Prerequisites
  - Python 3.8+
  - Virtualenv and Pip


## Project setup
  - First of all clone this Project
  - `cd <project_directory>`
  - `mkdir templates` and `mkdir static/media`
  - `python3.* -m venv <virtualenv_name>`
  - Activate `<virtualenv_name>`
    -  `source virtualenv_name/bin/activate` (*linux) 
    -  `virtualenv_name\Scripts\activate` (Windows)
  - Install packages `pip install -r requirements.txt`
  - Copy configure `copy "config.py sample" config.py`
    - `<Fillup your config.py file>`
  - Run `python manage.py migrate`
  - Run `python manage.py createsuperuser`
    - Provide `<username><email><password>`
  - Run `python manage.py makemigrations`


## How to Run this Project  
  - Run `python manage.py runserver` or
  - Run script `python manage.py <script_file_name --args args_value>`


## Helpful commands
  - `python manage.py makemigrations <app_name>` "for migration"
  - `python manage.py runserver host:port` "for starting dev. server"
  - `python manage.py startapp app_name` "for new app"
  - `python manage.py showmigrations` "To displays a list of all the migrations"
  - `python manage.py flush` "To command used to clear all data from the database associated with your Django project."


