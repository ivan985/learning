from django.urls import path

from .views import index_view, one_course_view, \
    edit_course_view, delete_course_view, \
    contacts_view, \
    CourseCreateView, CourseDetailView, CourseListView

app_name = 'mycourse'

urlpatterns = [
    # Function based views
    path('', index_view, name='index'),
    path('contacts/', contacts_view, name='contacts'),
    path('one_course/<int:pk>/', one_course_view, name='one_course'),
    path('one_course/<int:pk>/delete_course/', delete_course_view, name='delete_course'),
    path('one_course/<int:pk>/edit_course/', edit_course_view, name='edit_course'),

    # Class based views
    path('create_course/', CourseCreateView.as_view(), name='create_course'),
    path('one_course/<int:pk>/view/', CourseDetailView.as_view(), name='one_course_view'),
    path('view/', CourseListView.as_view(), name = 'index_view')
]