   cd myblog/
 apt install python3-django python3-pip python3-venv nginx e  
  python3 manage.py runserver
  
  apt install gunicorn
  
   nohup gunicorn --bind 127.0.0.1:8000 myblog.wsgi:application > gunicorn.log 2>&1 &

    cd myblog
 
 django-admin startproject myblog
 cd myblog
  
 python3 manage.py startapp blog
   
   
   python3 manage.py migrate
  python3 manage.py makemigrations
  
  python3 manage.py createsuperuser
  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


docker build -t my_resume .
docker run -d -p 8000:8000 my_resume
