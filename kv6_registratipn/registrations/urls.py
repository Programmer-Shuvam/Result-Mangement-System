from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.category_selection, name="category_selection"),
    path('selectionpage/', views.category_selection, name="category_selection"),
    path('thank_u/', views.thanku, name="thanku"),
    path('teacherarea/', views.thanku, name="login"),
    path('upload/', views.upload, name="upload"),
    path('login/', views.login, name="login"),
    path('student_registration/', views.student_registration,
         name="student_registration"),
    path('submit/', views.submit, name="submit"),
    path('thanx/', views.thanx, name="thanx"),
]