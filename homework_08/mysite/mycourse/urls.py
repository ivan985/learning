from django.urls import path

from .views import index_view, one_course_view, create_course_view, edit_course_view, delete_course_view

app_name = 'mycourse'

urlpatterns = [
    path('', index_view, name='index'),
    path('create_course/', create_course_view, name = 'create_corse'),
    path('one_course/<int:pk>/', one_course_view, name='one_course'),
    path('one_course/<int:pk>/delete_course/', delete_course_view, name='delete_course'),
    path('one_course/<int:pk>/edit_course/', edit_course_view, name='edit_course')
]