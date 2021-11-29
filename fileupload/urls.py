from django.urls import path
from fileupload import views
app_name="fileupload"

urlpatterns=[
    path('',views.fileinput,name='home'),
    path('userdata',views.userData,name='saveddata'),
    path('logout',views.userLogout,name='logout'),
]