import django
from django.db.models import F

django.setup()

from mycourse.models import Student


def update_student_year():

    student = Student.objects.first()
    student.course_year += 1
    student.save()


def update_student_year_extended():
    student = Student.objects.first()
    student.course_year = F('course_year') + 1
    student.save()


# populate_db()
update_student_year()
update_student_year_extended()