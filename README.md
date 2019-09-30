## Install Rabbit-MQ:
```brew services start rabbitmq```

### Launch worker (either from venv or not):
```celery worker --concurrency 2 -A celery_lab -Q lab.generate_and_sum_of_lists```

--concurrency - число дочерних процессов в Воркере, дефолт: 4
-A - название проекта
-Q - перечисляем названия очередей. Например, -Q SMS,email. Или -Q SMS,email,hard_task

-----------------------------

Ссылка на RabbitMQ:
http://127.0.0.1:15672/#/queues
Логин и пароль: guest
