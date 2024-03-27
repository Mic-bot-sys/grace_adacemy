from django.urls import path

from grace_forte_app.views.CourseViews import *

urlpatterns = [
    path('get/', GetCourses, name="get_courses"),
    path('get/<str:id>/', GetCourseById, name="get_course"),
    path('post', CreateCourse, name="create_course"),
    path('put/<str:id>', UpdateCourse, name="update_course"),
    path('delete/<str:id>', DeleteCourse, name="delete_course"),
]