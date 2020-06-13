from django.contrib import admin
from .models import Course, Teacher, Lesson

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "complexity", "time_created"
    list_display_links = ["title"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "full_name", "email"
    list_display_links = ["full_name"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = "id", "title", "course_title", "number_in_course", "course_teacher"
    list_display_links = ["title"]
