import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

celery_app = Celery('my_shop', broker='redis://localhost:6379/0')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
