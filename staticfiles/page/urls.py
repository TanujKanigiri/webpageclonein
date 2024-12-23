from django.urls import path
from .views import *

app_name='webpage'

urlpatterns = [
    path('',home,name="home"),
    path('courses/',courses,name="courses"),
    path('bootcamp/',bootcamp,name="bootcamp"),
    path('request/',request,name="request"),
    path('signin/',signin,name="signin"),
    path('checkcourses/',checkcourses,name="checkcourses"),
]
