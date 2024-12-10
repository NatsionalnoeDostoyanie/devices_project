# The Devices Project
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![python](https://img.shields.io/badge/python-3.12-3776AB.svg?style=flat&logo=python&labelColor=%23ccfcec)](https://www.python.org)
[![Static Badge](https://img.shields.io/badge/django-5.1-blue?logo=django&logoColor=green&labelColor=%23ccfcec)](https://docs.djangoproject.com/en/5.1/)
[![Static Badge](https://img.shields.io/badge/djangorestframework-3.15-blue?logo=django&logoColor=green&labelColor=%23ccfcec)](https://pypi.org/project/djangorestframework/)
[![Static Badge](https://img.shields.io/badge/docker-27.3-blue?logo=docker&logoColor=%232496ED&labelColor=%23ccfcec)](https://www.docker.com/)
[![Static Badge](https://img.shields.io/badge/redis-7.4-blue?logo=redis&logoColor=%23FF443&labelColor=%23ccfcec)](https://redis.io/)
[![Static Badge](https://img.shields.io/badge/postgresql-17-blue?logo=postgresql&logoColor=%232496ED&labelColor=%23ccfcec)](https://www.postgresql.org/)

## Table of Contents
- [Set up and run](#set-up-and-run)
- [Auth](#Auth)
- [URLs](#urls)

## Set up and run

Before you can run the application you will need to rename the [`.env.template`](.env.template) file to `.env` and then configure it:
```ini
# Dadata

DADATA_API_KEY = <YOUR_API_KEY>

DADATA_SECRET_KEY = <YOUR_SECRET_KEY>
```

To run the application you need to go to `devices_project/` and then run:
```bash
make docker-compose-build-and-up
```

The `Django superuser` will be automatically created with this data (you can change it):
```ini
# Django

SUPERUSER_NAME = "some_superuser_name"

SUPERUSER_EMAIL = "some_superuser_email@gmail.com"

SUPERUSER_PASSWORD = "some_superuser_password"
```

> [!WARNING]
> You have to delete the `docker-compose-stack` (all containers) every time you stop it

## Auth

Make the `POST-request` to the \
http://127.0.0.1:8000/api/v1/token/ 

With the `body`:
```json
{
    "username": "some_superuser_name",
    "password": "some_superuser_password"
}
```

You will get:
```json
{
    "token": "<Token you have get>"
}
```

Add the `Authorization` header to all your next requests:
```
GET ... HTTP/1.1
Host: 127.0.0.1:8000
...
...
...
Authorization: Token <Token you have get>
```

## URLs

You can `GET` next resources: 

 - **`All URLs related to the devices application`** 
 - - http://127.0.0.1:8000/api/v1/devices/
 - - - **Response example:**
```json
{
    "devices": "http://localhost:8000/api/v1/devices/devices/",
    "device-models": "http://localhost:8000/api/v1/devices/device-models/"
}
```


 - **`Device`** 
  - - Supporded **`Query Params`** for all these resources:
 - - - `limit` - must be an integer between *0* and *9,223,372,036,854,775,807*, otherwise takes **DEFAULT**
 - - - - **DEFAULT:** *9,223,372,036,854,775,807*
 - - - `offset` - must be a positive integer, otherwise takes **DEFAULT**
 - - - - **DEFAULT:** *0*
 - - **`All the device instances`**
 - - - http://127.0.0.1:8000/api/v1/devices/devices /
 - - - - **Response example:**
```json
{
    "meta": {
        "resultsCount": 2,
        "total": 2
    },
    "results": [
        {
            "id": 2,
            "address": "198515, г Санкт-Петербург, Красносельский р-н, Санкт-Петербургское шоссе",
            "name": "Device 2 name",
            "ipAddress": "2.2.2.2",
            "comment": "The comment",
            "model": null,
            "author": null
        },
        {
            "id": 1,
            "address": "101000, г Москва",
            "name": "Device 1 name",
            "ipAddress": "11.11.11.11",
            "comment": "",
            "model": null,
            "author": 1
        }
    ]
}
```
 - - **`All the device model instances`**
 - - - http://127.0.0.1:8000/api/v1/devices/device-models/
 - - - - **Response example:**
```json
{
    "meta": {
        "resultsCount": 2,
        "total": 2
    },
    "results": [
        {
            "id": 1,
            "name": "device model 1",
            "description": "description"
        },
        {
            "id": 2,
            "name": "device model 2",
            "description": "description"
        }
    ]
}
```

You can also go to the `admin-panel`: \
http://127.0.0.1:8000/admin/
