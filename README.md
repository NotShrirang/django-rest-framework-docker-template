# *****

DB Diagram: 

## .env file config (PostgreSQL):

```
DB_NAME = *****
DB_USER = *****
DB_PASS = *****
DB_HOST = *****
DB_PORT = *****
EMAIL = *****
EMAIL_PASSWORD = *****
```

## To run docker container:

```bash
./run.sh start-dev
```

## To manually start server:

## Install packages:

```bash
pip install -r requirements.txt
```

## Migrate to Database:

```bash
python manage.py migrate
```

## Run backend:

```bash
python manage.py runserver
```
