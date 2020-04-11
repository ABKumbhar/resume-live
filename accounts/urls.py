from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


    path('homepage/',views.homepage,name='home'),
    path('logout/',views.logoutuser,name='logout'),


    path('about/',views.about),
    path('register/',views.register),
    path('',views.loginpage,name='login'),
    path('feedback/',views.feedback,name='feedback'),
    path('myprojects/',views.myprojects),
    path('extracurricular/',views.extracurricular),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_complete"),

]
