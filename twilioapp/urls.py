from django.urls import path, include
from .views import *


app_name = 'twilioapp'


urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('register/', register, name='register'),
]
