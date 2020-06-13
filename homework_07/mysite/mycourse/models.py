from django.db import models

# Create your models here.


# Класс для курсов
class Course(models.Model):
    comp_low = 1
    comp_normal = 2
    copm_high = 3

    COMPLEXITY = (
        (comp_low, 'low'),
        (comp_normal, 'normal'),
        (copm_high, 'high'),
    )

    title = models.CharField(max_length=250)
    complexity = models.IntegerField(choices=COMPLEXITY)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Класс для преподавателей
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


# Класс для уроков
class Lesson(models.Model):
    title = models.CharField(max_length=250)
    number_in_course = models.IntegerField()

    course_title = models.ForeignKey(Course, on_delete=models.PROTECT)
    course_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
