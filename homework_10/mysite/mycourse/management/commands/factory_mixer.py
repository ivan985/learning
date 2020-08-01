
from mixer.backend.django import mixer
from django.core.management import BaseCommand

from mycourse.models import Course, Teacher, Lesson


def create_all():
    courses = mixer.cycle(20).blend(Course)
    teachers = mixer.cycle(20).blend(Teacher)
    lessions = mixer.cycle(20).blend(Lesson)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()