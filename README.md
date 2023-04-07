## The simple example of Django with Celery

#### Show log celery

```sh
celery -A TestCelery worker -l info
```

#### Use flower to see celery database
```sh
celery -A TestCelery flower  --address=127.0.0.6 --port=5566 --persistent=True --db=flower.db
```
