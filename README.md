## Celery lab
This repo shows example how to interact with celery and RabbitMQ

### Description of Lab:
`celery_lab/web/app.py` - publish message to one of the following queues: email, SMS or hard_task. It does in appropriate way to celery, so you won't be able to publish via web-interface because celery won't understand this

`celery_lab/celery.py` - entry point, it is running by default once you launch worker

`celery_lab/functions.py` - file with functions for testing perfomance

`celery_lab/tasks.py` - wrapped functions which are called by celery once it receives message from queue in Rabbit

`config.py` - it is imported from celery.py

### Launch worker (either from venv or not):
Just an example how to launch worker:

```celery worker --concurrency 2 -A celery_lab -Q lab.generate_and_sum_of_lists```

--concurrency - number of concurrent processes, default: 4

-A - name of project. In our case it is celery_lab

-Q - list queues you want to listen to. For example, -Q SMS,email or -Q SMS,email,hard_task

### Reminder about RabbitMQ:
https://github.com/DmitriiDenisov/rabbitmq_lab
