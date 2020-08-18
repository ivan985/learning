
from mixer.backend.django import mixer
from django.core.management import BaseCommand

from mycourse.models import Course, Teacher, Student


def create_teachers_and_students():
    teachers = mixer.cycle(20).blend(Teacher)
    students = mixer.cycle(20).blend(Student)


def create_courses():
    courses = mixer.cycle(20).blend(Course)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_teachers_and_students()
        create_courses()
