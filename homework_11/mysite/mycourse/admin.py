from django.contrib import admin
from .models import Course, Teacher, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "complexity", "time_created"
    list_display_links = ["title"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "full_name", "email"
    list_display_links = ["full_name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "full_name", "email"
    list_display_links = ["full_name"]
