from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page),
    path('register',views.register),
    path('login',views.login),
    path('post_register', views.post_register),
    path('post_login', views.post_login),
    path('user_page', views.user_page),
    path('champ_info/<int:id>', views.champ_info),

]