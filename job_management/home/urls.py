from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:number_week>', show_week, name='post'),
]