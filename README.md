## The simple example of Django with Celery

#### Start celery worker

`TestCelery` is the name of the project in this example.
```sh
celery -A TestCelery worker -l info
```
if facing `ValueError: not enough values to unpack (expected 3, got 0)`
```
celery -A TestCelery worker --pool=solo -l info
```
Or using `Eventlet` as your execution pool
```
pip install eventlet
celery -A TestCelery worker -l info -P eventlet
```
if `Eventlet` has an issue on subprocess.CalledProcessError. Try `gevent`
```
pip install gevent
celery -A TestCelery worker -l info -P gevent
```

#### Use flower to see celery database
```sh
celery -A TestCelery flower  --address=127.0.0.6 --port=5566 --persistent=True --db=flower.db
```


## To schedule task

1. Define a function to schedule using `app.task` decorator
    ```
    from TestCelery.celery import app
    
    @app.task
    def your_periodic_task():
        # Your periodic task logic here
        # This task will run at the specified interval
        print("This is a periodic task.")
    ```

2. Define the schedule for `your_periodic_task` using the `CELERY_BEAT_SCHEDULE` setting:
    ```
    from celery.schedules import crontab
    
    CELERY_BEAT_SCHEDULE = {
        'your_periodic_task_name': {
            'task': 'your_app_name.tasks.your_periodic_task',
            'schedule': crontab(minute='*/1'),  # Schedule the task to run every minute
        },
    }
    ```
3. Start celery beat

    ```celery -A TestCelery.celery beat --loglevel=info```

5. Start celery worker by following `Start celery worker` instruction.
