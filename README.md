# Question-Bank-Management-System

Question Bank Management System can be used to access the complete questions that were ever asked on various exams on different subjects of various departments across various universities.

This project is build using **Python Django** Framework.

> The deployed working link of the project is [here](https://questionbank.kripaelectrolysis.com/)

## Features

- view questions based on different categorisation, sorting, search questions based on various parameters
- questions will only appear after verification from admin, hence trustworthiness of the questions is maintained
- user friendly interface

## Installation

### Requirements
- Python 3.6 or above
- NodeJs and NPM (NodeJs is required for building the frontend part of the project using tailwindcss)

### Clone the repository
```bash
$ git clone https://github.com/ilyasbabu/question-bank-management-system.git
$ cd question-bank-management-system
```

### Install dependencies
```bash
$ pip install -r requirements.txt
```

### Setup the eviornment variables

Create a file named `.env` in the root directory of the project and add the following lines to it

```bash
# Django configuration
DEBUG = True
SECRET_KEY = '<secret_key>'

# Database configuration
DB_ENGINE = "<depends on the database you are using>"
DB_NAME = "<database_name>"
DB_USER = "<database_user>"
DB_PASSWORD = "<database_password>"
DB_HOST = "<database_host>"

# Tailwind configuration
NPM_PATH = "<path to npm>"
# on windows it might look like this r"C:\Program Files\nodejs\npm.cmd"
# on linux it might look like this "/usr/bin/npm"

# Mail configuration
EMAIL_HOST = "<email_host>"
EMAIL_PORT = "<email_port>"
EMAIL_USER = "<your email>"
EMAIL_PASSWORD = "<your email password>"
```

### Create the database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Create the admin user

```bash
$ python manage.py createsuperuser
```

### Start the server

```bash
$ python manage.py runserver
```

> For the frontend development, you should also start the tailwind server as well, so on other terminal

```bash
$ python manage.py tailwind install
$ python manage.py tailwind start
``` 


## Tech-stacks used

[<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>](https://www.python.org/)
&nbsp;&nbsp;
[<code><img height="30" src="https://avatars.githubusercontent.com/u/27804?s=200&v=4"></code>](https://www.djangoproject.com/) 
&nbsp;&nbsp;
[<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>](https://developer.mozilla.org/en-US/docs/Web/HTML) 
&nbsp;&nbsp;
[<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>](https://developer.mozilla.org/en-US/docs/Web/CSS)
&nbsp;&nbsp;
[<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 
&nbsp;&nbsp;
[<code><img height="30" src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_git-512.png"></code>](https://git-scm.com/downloads)
&nbsp;&nbsp;
[<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/postgresql/postgresql.png"></code>](https://www.postgresql.org/) 
&nbsp;&nbsp;
[<code><img height="30" src="https://avatars.githubusercontent.com/u/67109815?s=200&v=4"></code>](https://tailwindcss.com/) 
&nbsp;&nbsp;

## Future Improvements

- [ ] Need to make categorisation, sorting and searching robust without page reload.
- [x] Need to implement a feature of selecting questions and printing them.
- [ ] Need to improve the UI and implement Dark Theme.
- [ ] Need to implement a new interface for admins and moderators.
- [ ] Need to implement rich text formatting for question answers.
- [ ] Need to implement OAuth.
- [ ] Need to Optimize the build.

## License

Free to use and modify, just ⭐.

<p align="center">
 <img src="https://c.tenor.com/Ew3ZGdPEOTcAAAAd/remus-lupin.gif" /> </br></br> 
 <span> Made with ❤ </span>      
</p>