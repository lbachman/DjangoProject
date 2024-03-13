# Social Media App with React and Django

# Overview 
This project aims to build a social media application where users can create profiles, post updates, follow other users, like and comment on posts, and engage in social interactions. The application will consist of a front end developed using React for the user interface and a back end implemented with Django to handle data storage, user authentication, and API endpoints.

## Requirements

### Django
- `pip install Django`

### MySQL Connector 
-  `pip install mysql-connector-python`

### mysqlclient
- `pip install mysqlclient`

### djangocruds
- `pip install django-cruds-adminlte`

### djangorestframework
- `pip install djangorestframework`

pip install django-cors-headers





# Useful Virtual Environment Commands
- **Install venv**
    - Unix: `python -m venv {desired name}`
    - Windows: `py -m venv {desired name}`
- **Activate venv**
    - Unix: `source venv/bin/activate`
    - Windows: `\Scripts\activate.bat` (Use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` on PowerShell to allow permission)
- **Deactivate venv**
    - Windows: `deactivate`
    - Unix: `conda deactivate`
- **Create Requirements file**
    - `pip freeze > requirements.txt` generates requirements file 
    - `pip install -r requirements.txt` installs all packages in requirements.txt file 

#### *Remember that the venv file should be specified in the .gitignore file*
#### *It is also good pratice to install the venv in the same directory as the manage.py file*

# Django Commands 
- `django-admin startproject {project name}` creates the Django project
    - this should create a new directory with the specified project name and this file structure: 
        ``` 
            {project name}/
            ├── manage.py
            └── myproject/
                ├── __init__.py
                ├── settings.py
                ├── urls.py
                └── wsgi.py
        ```
           
- `py manage.py runserver` starts the server (make sure you are in the same directory as the manage.py file.)
- `py manage.py startapp {app name}` creates the app
- `py manage.py makemigrations {app name}` create migration files based on the changes you've made to your models
- `py manage.py migrate` - applies any changes made to the models in python to the database schemas.
- `py manage.py sqlmigrate {app name} {migration number ie 0001}` view sql statement executed from migration.

# Working with SQLite (not currently used in this project)
- `py manage.py shell` opens python shell
    - `from {app name}.models import {model name}` - imports model name
    - `member = Member(firstname='Logan', lastname='Bachman')` adds record to table
    - `member.save()` saves record. must be done on each entry
    - `{model name}.objects.all().values()` prints all entries in table
    - `from {app name}.models import {model name}`
    - `x = {model name}.objects.all()[index #]` stores reference to object in database as variable
    - `x.delete()` deletes record from table

# Working with MySQL
- to establish connection to MySQL database, go to the *settings.py* file located in the project file and edit the following code: 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{put schema name here}',
        'USER': 'put user name here ie "root"',
        'PASSWORD': '{password to server}',
        'HOST': '127.0.0.1',  # Set to your MySQL host
        'PORT': '3306',       # Set to your MySQL port (default is 3306)
    }
}
```

# Adding data to database
- first create the models in the models page of the app
- make sure to specify that the app is installed in the settings.py file under INSTALLED APPS
- run `py manage.pymakemigrations {app name}` and then `py manage.py migrate`

# Creating Controller
- run `py manage.py cruds`

# FrontEnd in React
- npm install react-scripts --save-dev
- 
- 

