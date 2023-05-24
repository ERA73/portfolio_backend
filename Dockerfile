# Set image
FROM python:3.9-slim
RUN pip install --upgrade pip 
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

# Set continer work directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Migrate
RUN python manage.py makemigrations 
RUN python manage.py migrate

# Collects static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for django
EXPOSE 8000

# Serve django app
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]



# FROM python:3.9-slim
# RUN pip install --upgrade pip 
# RUN apt-get update
# RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY . /app
# WORKDIR /app
# COPY ./entrypoint.sh .
# ENTRYPOINT ["sh", "/app/entrypoint.sh"]