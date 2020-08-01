from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Course, Teacher, Lesson
from .forms import CourseForm, ContactForm
from django.views.generic import CreateView, DetailView, ListView
from django.core.mail import send_mail
from .serializers import CourseSerializer, TeacherSerializer, LessonSerializer
import django_rq

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SecretView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        data = {"message": "Secret text"}
        return Response(data)


def index_view(request):
    context = {'all_courses': Course.objects.all()}
    return render(request, 'index.html', context=context)


def one_course_view(request, pk):
    context = {'one_course': Course.objects.filter(pk = pk).first()}
    return render(request, 'one_course.html', context=context)


def delete_course_view(request, pk):
    course = Course.objects.filter(pk=pk).first()  # если в course лежит None, то выводится пустая форма
    if request.method == 'GET':
        form = CourseForm(instance=course)
    elif request.method == 'POST':
        form = CourseForm()
        if course:
            course.delete()
    return render(request, 'delete_course.html', context={"form": form})


def edit_course_view(request, pk):
    course = Course.objects.filter(pk=pk).first()
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
    return render(request, 'edit_course.html', context={"form": form})


def contacts_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']

        recipients = ['admin@example.com']

        django_rq.enqueue(send_mail, subject, message, sender, recipients)

        new_subject = 'Your mail to mycourse'
        new_message = 'Your mail to mycourse has been sended'
        new_sender = 'admin@example.com'
        new_recipients = [sender]

        django_rq.enqueue(send_mail, new_subject, new_message, new_sender, new_recipients)

    return render(request, 'contacts.html', context={"form": form})


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'

    def get_success_url(self):
        return '/index/one_course/{}/'.format(self.object.pk)


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 100


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
