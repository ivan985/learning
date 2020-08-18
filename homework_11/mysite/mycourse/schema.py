import graphene
from graphene_django.types import DjangoObjectType

from .models import Course, Teacher, Student


class CourseType(DjangoObjectType):

    class Meta:
        model = Course


class TeacherType(DjangoObjectType):

    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):

    class Meta:
        model = Student


class Query:
    all_courses = graphene.List(CourseType)
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)

    def resolve_all_courses(self, *args, **kwargs):
        return Course.objects.all()

    def resolve_all_teachers(self, *args, **kwargs):
        return Teacher.objects.all()

    def resolve_all_students(self, *args, **kwargs):
        return Student.objects.all()
