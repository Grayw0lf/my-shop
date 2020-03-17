from my_shop.celery import celery_app
from django.core.mail import send_mail
from .models import Order


@celery_app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ c номером {}'.format(order.id)
    message = 'Дорогой, {}, вы успешно сделали заказ.\
                   Номер вашего заказа {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'admin@myshop.ru', [order.email])
    return mail_send
