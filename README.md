## Celery lab
This repo shows example how to interacte with celery and RabbitMQ

### Launch worker (either from venv or not):
Just an example how to launch worker:
```celery worker --concurrency 2 -A celery_lab -Q lab.generate_and_sum_of_lists```

--concurrency - число дочерних процессов в Воркере, дефолт: 4
-A - название проекта
-Q - перечисляем названия очередей. Например, -Q SMS,email. Или -Q SMS,email,hard_task
