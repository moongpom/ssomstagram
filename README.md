# ssomstagram

git clone https://github.com/moongpom/ssomstagram.git

git clone 한 뒤에 순서대로 입력하기

git init

python -m venv myvenv

source myvenv/Scripts/activate

cd ssomstagram

pip install django

pip install django-allauth

pip install pillow

pip install simplejson

pip install django-rest-framework

pip install gunicorn whitenoise dj-database-url psycopg2-binary

pip install django-storages boto3

python manage.py makemigrations

python manage.py migrate


python manage.py runserver
