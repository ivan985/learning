from rest_framework import serializers
from .models import Course, Teacher, Student


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        view_name = 'course'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        view_name = 'teacher'


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        # lookup_field = 'course'
        view_name = 'lesson'
