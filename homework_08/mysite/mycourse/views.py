from django.http import HttpResponse
from django.shortcuts import render
from .models import Course
from .forms import CourseForm


def index_view(request):
    context = {'all_courses': Course.objects.all()}
    return render(request, 'index.html', context=context)


def one_course_view(request, pk):
    context = {'one_course': Course.objects.filter(pk = pk).first}
    return render(request, 'one_course.html', context=context)


def create_course_view(request):
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'create_course.html', context={"form": form})
    elif request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_course.html', context={"form": form})


def delete_course_view(request, pk):
    if request.method == 'GET':
        course = Course.objects.filter(pk=pk).first()
        form = CourseForm(instance=course)
        return render(request, 'delete_course.html', context={"form": form})
    elif request.method == 'POST':
        form = CourseForm()
        course = Course.objects.filter(pk=pk).first()
        if course:
            course.delete()
        return render(request, 'delete_course.html', context={"form": form})


def edit_course_view(request, pk):
    if request.method == 'GET':
        course = Course.objects.filter(pk=pk).first()
        form = CourseForm(instance=course)
        return render(request, 'edit_course.html', context={"form": form})
    elif request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'edit_course.html', context={"form": form})