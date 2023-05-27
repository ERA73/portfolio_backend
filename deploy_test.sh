git pull origin develop \
&& source env/bin/activate \
&& pip install -r requirements.txt \
&& python manage.py makemigrations contact \
&& python manage.py migrate