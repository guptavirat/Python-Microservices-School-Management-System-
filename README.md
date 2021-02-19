# School Management System - Microservice

It has two microservices added-
1. Web portal to see the dashboard of courses and student details running on port 5000.
2. Login portal for student and new student registration running on port 5001.

#### Prerequsites

Check that you have installed following:

* Python >= 3.5

#### Getting started

After you clone repo to your local computer, navigate to newly created
directory and do the following steps:

1. Create Virtualenv

   ```
   $ virtualenv env
   ```

   This will create `env` directory inside project. Don't worry,
   it's ignored by GIT by default.

2. Activate Virtualenv for the project

   ```
   $ source ./env/bin/activate
   ```

   This will activate local development environment in current terminal
   session only. You have to run this command for every new terminal session.

   You should notice `(env)` text at the beginning of your command line prompt.

3. Install requirements
   ```
   (env) $ pip install -r requirements.txt
   ```

4. Run migrations in order to create db and tables

   ```
   (env) $ python manage.py db upgrade
   ```
   
5. Create empty database 
``` open cmd and navigate to flask-simple-login folder
cd flask-simple-login/
python
>>> from login_app import create_db
>>> create_db()
>>> exit()

run database server
on command prompt type python login_app.py once server is up, leave the prompt as it is.
```

6. Run server - Open another command prompt from root directory (where manage.py file exist)

   ```
   python manage.py runserver
   ```

7. Open web-browser and navigate to http://localhost:5000

8. To start Student registration and login portal navigate to flask-simple-login-master folder on command prompt and run

   ```
   python login_app.py
   ```


## Documentation

All documentation can be found in [doc](doc/README.md) directory.

## To add/append the database fields.
1. Edit file- index.html and form.html from respective module
2. edit file- models, controllers and forms.py from respective module.
3. update create table.py (respective module) from migrations folder.
#to execute-
1. rename app.db to old_app.db
2. delete old tables from migrations\versions\__pycache__
3. run db upgrade command and restart server