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


class Lesson(AbstractModel):
    """
    Класс для уроков
    """
    title = models.CharField(max_length=250)
    number_in_course = models.IntegerField()

    course_title = models.ForeignKey(Course, on_delete=models.PROTECT)
    course_teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)

