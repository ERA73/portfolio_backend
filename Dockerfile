FROM python:3.9-slim
RUN mkdir /app
WORKDIR /app
COPY . .
RUN apt-get update \
        && apt-get install -y python3-pip \
        && pip install --upgrade pip \
        && apt-get install python3-dev default-libmysqlclient-dev gcc  -y  \
        && pip install --no-cache-dir -r requirements.txt \
        && pip install --no-cache-dir gunicorn

EXPOSE 8000

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]