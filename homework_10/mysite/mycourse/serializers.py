from rest_framework import serializers
from .models import Course, Teacher, Lesson


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'url', 'title', 'complexity', 'time_created')
        view_name = 'course'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        view_name = 'teacher'


class LessonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        # lookup_field = 'course'
        view_name = 'lesson'
