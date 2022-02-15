from django.urls import path, include

from main import views

urlpatterns = [
    path('getAge/', views.getAge),
]