from django.urls import path
from django.contrib.auth import views as auth

#from .views import home
from .views import *
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='project_app/index.html'), name='logout'),
    path('', index,name='index'),
]