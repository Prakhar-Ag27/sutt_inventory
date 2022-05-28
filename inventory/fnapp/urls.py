from django.urls import path

from . import views

urlpatterns = [
    path('', views.details, name='details'),
    path('issue/', views.issue, name='details'),
]