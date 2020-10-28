from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from .views import (
    index_view,
    students_view,
    students_upd,
    students_dwn,
    one_course_view,
    edit_course_view,
    delete_course_view,
    contacts_view,
    CourseCreateView,
    CourseDetailView,
    CourseListView,
    CourseViewSet,
    TeacherViewSet,
    StudentViewSet,
    SecretView
    )

# app_name = 'mycourse'

router = DefaultRouter()
router.register('course', CourseViewSet)
router.register('teacher', TeacherViewSet)
router.register('student', StudentViewSet)

urlpatterns = [
    # Function based views
    path('', index_view, name='index'),
    path('view/', students_view, name='students'),
    path('view/upd', students_upd, name='students'),
    path('view/dwn', students_dwn, name='students'),
    path('contacts/', contacts_view, name='contacts'),
    path('one_course/<int:pk>/', one_course_view, name='one_course'),
    path('one_course/<int:pk>/delete_course/', delete_course_view, name='delete_course'),
    path('one_course/<int:pk>/edit_course/', edit_course_view, name='edit_course'),

    # Class based views
    path('create_course/', CourseCreateView.as_view(), name='create_course'),
    path('one_course/<int:pk>/view/', CourseDetailView.as_view(), name='one_course_view'),
    path('secret/', SecretView.as_view(), name='secret_view'),

    # Router
    path('api/', include(router.urls), name='index_view'),

    # Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
