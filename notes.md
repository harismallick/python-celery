## Command to initiate redis using docker:

### Requirements for celery to work with a backend db:
```bash
    pip install celery
    # If celery is ran with a broker:
    pip install redis
    # If celery is used with a backend db:
    pip install SQLAlchemy
    # if the backend db is postgresql:
    pip install psycopg2-binary
```
```bash
    docker run -p 6379:6379 -d redis
```
Celery is not linked to the application itself. Similar to gunicorn, you pass the application to Celery.
```bash
    python3 -m celery -A <py-file-with-celery-object> worker --loglevel=INFO
```

Store the queued processed and the state of these processes in a backend db. Postgres is a good option.
Initialise postgres either locally or in a container.
```bash
    docker run -p 5433:5432 -e POSTGRES_PASSWORD=password -d postgres

    # If no local instance of postgres exists, then port 5432 can be used for the host.
```
