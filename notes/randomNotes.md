# Requirements
## Django
- Windows: `py -m pip install Django`
- Unix: `python -m pip install Django`
## MySQL Connector 
- Windows: `pip install mysql-connector-python`

## mysqlclient
- Windows: `pip install mysqlclient`


# Useful Virtual Environment Commands
- Install venv
    - Unix: - `python -m venv myworld`
    - Windows: - `py -m venv myworld`
- Activate venv   
    - Unix: `source venv/bin/activate`
    - Windows: `\Scripts\activate.bat`
        - Use this command to allow on powershell: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
- Deactivate venv
    - `deactivate`
    - `conda deactivate`
- Create Requirements file
    - `pip freeze > requirements.txt` generates requirements file 
    - `pip install -r requirements.txt` installs all packages in requirements.txt file


### *Remember that the venv file should be specified in the .gitignore file*

# Django Commands 
- `django-admin startproject {project name}` creates the Django project
- `py manage.py runserver` starts the server
- `py manage.py startapp {app name}` creates the app
- `py manage.py migrate` - unsure 
- `py manage.py makemigrations {app name}` creates the table in the database (run command in root folder)
- `py manage.py sqlmigrate {app name} {migration number ie 0001}` view sql statement executed from migration.
- `py manage.py makemigrations`


# Working with SQLite
- `py manage.py shell` opens python shell
    - `from {app name}.models import {model name}` - imports model name
    - `member = Member(firstname='Logan', lastname='Bachman')` adds record to table
    - `member.save()` saves record. must be done on each entry
    - `{model name}.objects.all().values()` prints all entries in table
    - `from {app name}.models import {model name}`
    - `x = {model name}.objects.all()[index #]` stores reference to object in database as variable
    - `x.delete()` deletes record from table 