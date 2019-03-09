# Forum
My first project in Python Django
The forum has only basics functions:
- Login and registration
- Posts list on the home page - each post has its own category
- Simple user panel - you can change your password and see your posts list from there
- You can add an answer to someone's question

**Modules used**
- Python 3.6.5
- Django 2.1.1
- mysqlclient 1.3.12
- pip 18.0

**Installation**
1.Install Forum using this command
```
git clone https://github.com/Incybro/Forum.git
```
2.Configure your database connection Forum/Forum/settings.py
```
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'forum',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': '',
}}
```
3.Aplly all migrations using command
```
python manage.py migrate
```
4.Run your Forum using command
```
python manage.py runserver
```
