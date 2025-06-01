from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>', reset_password_view, name='reset-password'),
    path('logout/', reset_password_view, name='logout'),
]