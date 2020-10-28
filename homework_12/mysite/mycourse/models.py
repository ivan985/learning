from django.db import models


class AbstractModel(models.Model):
    """
    Общий вывод для всех классов
    """
    class Meta:
        abstract = True

    def __str__(self):
        data = [f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')]
        return f'{self.__class__.__name__}({", ".join(data)})'

    def __repr__(self):
        return str(self)


class Teacher(AbstractModel):
    """
    Класс для преподавателей
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(AbstractModel):
    """
    Класс для cтудентов
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    course_year = models.IntegerField(default=1)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Course(AbstractModel):
    """
    Класс для курсов
    """
    COMP_LOW = 1
    COMP_NORMAL = 2
    COMP_HIGH = 3

    COMPLEXITY = (
        (COMP_LOW, 'low'),
        (COMP_NORMAL, 'normal'),
        (COMP_HIGH, 'high'),
    )

    title = models.CharField(max_length=250)
    complexity = models.IntegerField(choices=COMPLEXITY)
    time_created = models.DateTimeField(auto_now_add=True)

    teachers = models.ManyToManyField(Teacher, blank=True)
    students = models.ManyToManyField(Student, blank=True)