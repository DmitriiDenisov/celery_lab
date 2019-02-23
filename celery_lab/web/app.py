from celery_lab.tasks import send_email, send_sms
from random import randint


def email_and_sms():
    send_email.apply_async(queue='email')
    send_sms.apply_async(queue='SMS')
    return True


def email():
    send_email.apply_async(queue='email')
    return True


if __name__ == '__main__':
    thresh = randint(0, 9)
    if thresh < 4:
        print(1)
        A = email_and_sms()
    else:
        print(2)
        A = email()

    print(A)