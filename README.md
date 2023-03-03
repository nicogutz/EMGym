# Backend

## 1. Table of Contents

1. [Table of Contents](#1-table-of-contents)
2. [Introduction](#2-introduction)
    1. [File Structure](#21-file-structure)
3. [Routing](#3routing)
4. [Core](#4core)
5. [API](#5api)

## 2. Introduction

This **Django** project is meant to handle the whole backend. It should be the single source of truth for everything.
It will ingest data from the Raspberry Pi, put it in a database, and make it available to
a user.

To start, use Pycharm to make a new Virtual Environment and install the requirements.txt.

> ### 2.1 File Structure

```
├── apps
│   ├── api
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── factories.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   └── serializers.py
│   ├── __init__.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

> ### 2.2 Setup

## 3. Routing
Django works by directing endpoints to their respective views. In the backend you will be able to enter the Swagger 
view to test and understand the API endpoints. You can also access the admin console using the /admin/ endpoint.


## 4. Core
Here is where the main models of the database live. For every model you write, write a factory and a serializer for it.

## 5. API
We are using django_rest_framework to build the API. This makes for a really straightforward implementation.
Be sure to write unit tests for all the views.



