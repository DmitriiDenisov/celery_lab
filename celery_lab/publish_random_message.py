from celery_lab.tasks import send_email, send_sms, hard_func
from random import randint


def email_and_sms():
    send_email.apply_async(queue='email')
    send_sms.apply_async(queue='SMS')
    return True


def email():
    send_email.apply_async(queue='email')
    return True


def publish_hard_func(n, m):
    hard_func.apply_async((n, m), queue='hard_task')
    return True


if __name__ == '__main__':
    thresh = randint(0, 9)
    if thresh < 3:
        print(1)
        A = email_and_sms()
    elif 3 <= thresh <= 5:
        print(2)
        A = email()
    else:
        print(3)
        A = publish_hard_func(n=500, m=3000)

    print(A)
