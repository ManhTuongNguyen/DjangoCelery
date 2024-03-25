## The simple example of Django with Celery

#### Show log celery

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
