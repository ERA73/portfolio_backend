git pull origin features \
&& source env/bin/activate \
&& pip install -r requirements.txt \
&& python manage.py makemigrations contact \
&& python manage.py migrate