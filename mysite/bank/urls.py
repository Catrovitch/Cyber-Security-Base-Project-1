from django.urls import path

from . import views

app_name = 'bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/register_user/', views.register_user, name='register_user'),
    path('account_information/', views.account_information, name='account_information')
]