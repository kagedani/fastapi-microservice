# fastapi-microservice
Lightweight microservice example with Python FastAPI

##  Description

This is a basic python api application using the FastAPI framework. 

It implements a simple movie service to CRUD movies of a store. 

It is deployable locally on bare metal or on docker using [docker compose](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiYndWl-uOAAxWXQ_EDHWF-CH0QFnoECAYQAQ&url=https%3A%2F%2Fdocs.docker.com%2Fcompose%2F&usg=AOvVaw02oes91geDSZ-H__u_XMxc&opi=89978449).


###  Directory Structure
```
fastapi-microservice
├── docker-compose
│   ├── database_only
│   │   └── docker-compose.yaml
│   └── docker-compose.yaml
├── movie-service
│   ├── app
│   │   ├── api
│   │   │    ├── configs.py
│   │   │    ├── db_manager.py
│   │   │    └── movies.py
│   │   ├── config
│   │   │    └── config.py
│   │   ├── data
│   │   │    ├── db.py
│   │   │    └── Movie.py
│   │   └── __init__.py
│   ├── .env_default
│   ├── .env_local
│   ├── .env_test
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── conftest.py
├── .gitignore
├── README.md
└── environment.yml
```

###  Features

-  Automatic API documentation

- Containerization and portability

##  Getting Started

###  Getting Started with Docker compose

Getting started testing and extending this application is pretty simple using docker and docker-compose.

```shell script
# Clone the repository
git clone https://github.com/kagedani/fastapi-microservice.git

# cd into project root
cd fastapi-microservice/docker-compose

# Launch the project
docker-compose up -d
```

Afterwards, the project will be live at [http://localhost:8000](http://localhost:8000).

The docker compose include both the  Python application and a Postgres database container instance. 

##  Getting Started on bare metal

First of all, clone the repository

```shell script
# Clone the repository
git clone https://github.com/kagedani/fastapi-microservice.git

# cd into project root
cd fastapi-microservice
```

After this, you can set up the database container only using the docker-compose file located ad 
```
/fastapi-microservice/docker-compose/database_only/
```

using the `docker compose up -d` command. 

At this point you're ready to install in your local virtual env or using your pip installation directly the requirements:
```
pip install -r requirements.txt
```

Then using python directly or exploiting an IDE like VS or Pycharm the application can be run. 

**N.B.** You need to export the environment variable env=local if you want to run it locally, since the application use a .env file to get settings values.
