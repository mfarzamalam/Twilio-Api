from django.urls import path, include
from .views import *


app_name = 'twilioapp'


urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('register/', register, name='register'),
    path('checkout/', checkout, name='checkout'),
    path('finish/', finish, name='finish'),
    path('log_out/', log_out, name='log_out')
]
