bash - ниже запуск для Терминала
## Чтобы установить Rabbit-MQ:
brew services start rabbitmq

(чтобы из venv)
    # В консольке сначала cd в папку с проектом: затем:
    source venv/bin/activate

    # Далее запуск Worker'a:
    celery worker --concurrency 2 -A celery_lab -Q lab.generate_and_sum_of_lists
(чтобы без venv)
    В консольке сначала cd в папку с проектом: затем:
    celery worker --concurrency 2 -A celery_lab -Q lab.generate_and_sum_of_lists

--concurrency - число дочерних процессов в Воркере, дефолт: 4
-A - название проекта
-Q - перечисляем названия очередей. Например, -Q SMS,email. Или -Q SMS,email,hard_task

-----------------------------

Ссылка на RabbitMQ:
http://127.0.0.1:15672/#/queues
Логин и пароль: guest

Примеры запросов (через Postmaster)
http://127.0.0.1:5000/email_and_sms
http://127.0.0.1:5000/stupid-task
http://127.0.0.1:5000/home