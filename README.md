# My Resume Website

This is a simple Django-based web application for showcasing my resume. It includes a login page that redirects to the resume page upon successful authentication.

## Features
- **Login System**: Secure login functionality using Django's built-in authentication system.
- **Resume Display**: Shows the resume only to authenticated users.

## Requirements

Before you begin, ensure you have the following installed on your system:

- Python 3.8+
- Django 4.x
- Virtualenv (optional but recommended)

## Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/my_resume_website.git
cd my_resume_website
apt install python3-django python3-pip python3-venv nginx
python -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\activate`
 django-admin startproject myblog
pip install -r requirements.txt
python manage.py migrate
python3 manage.py makemigrations
python manage.py createsuperuser
docker build -t my_resume .
docker run -d -p 8000:8000 my_resume
my_resume_project/
├── manage.py
├── my_resume_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── resume/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── templates/
    │   ├── login.html
    │   └── resume.html
    ├── migrations/
    └── tests.py
      
