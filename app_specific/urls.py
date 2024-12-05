from app_specific.views import *
from django.urls import path

app_name='login1'

urlpatterns=[
    path('login/',login,name='login'),
]