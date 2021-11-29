from django.urls import path
from user_app import views

app_name='user_app'

urlpatterns = [
    path('register',views.registerpage,name='register'),
    path('',views.loginpage,name='login'),
]