from django.core.management import BaseCommand
from datetime import datetime
import django_rq
from mycourse.test_job import update_currency_rates


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        scheduler = django_rq.get_scheduler('default')
        job = scheduler.enqueue_at(datetime.utcnow(), func=update_currency_rates)
        print('run')
