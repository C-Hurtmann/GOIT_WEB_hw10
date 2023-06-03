from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
    ]