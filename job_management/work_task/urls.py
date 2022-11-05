from django.urls import path
from .views import *

urlpatterns = [
    path('', work_task, name='work_task'),
]