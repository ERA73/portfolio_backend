# Get Started
* Config the database runing the following commands:
    ``` 
    python manage.py makemigrations contact 
    python manage.py migrate 
    ```
* Install all dependencies runing the following command:
    ``` 
    pip install -r requirements.txt 
    ```
* Create django admin:
    ``` 
    python manage.py createsuperuser 
    ```
    * you only need to set the ***username*** and ***password***

# Docker
* Load docker file for the frontend:
    ``` 
    docker build -t portfolio_frontend_img -f Dockerfile . 
    ```
* Load docker file for the backend:
    ``` 
    docker build -t portfolio_backend_img -f Dockerfile . 
    ```
NOTE: Each command needs to be executed into the directory where is the file Dockerfile
* By deploy the project, only run the docker compose file with the next command:
    ```
    docker-compose up --build 
    ```
