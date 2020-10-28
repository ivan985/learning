import time

import django
import os
from django.core.management import BaseCommand

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# django.setup()


from mycourse.models import Student


def dummy_update():
    for student in Student.objects.filter(course_year=1):
        student.course_year = 2
        student.save()


def bulk_update():
    print("STARTED")
    time.sleep(1)
    Student.objects.filter(course_year=2).update(course_year=3)


class Command(BaseCommand):
    def handle(self, *args, **options):
        dummy_update()
        time.sleep(3)
        bulk_update()