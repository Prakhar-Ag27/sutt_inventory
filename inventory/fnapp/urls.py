from django.urls import path

from . import views

urlpatterns = [
    path('', views.details, name='details'),
    path('<int:itemcode>/', views.issue, name='issue'),
    path('success/<int:itemcode>/', views.success, name='success'),
    path('logadd/', views.log_add, name='logadd'),
    path('logtransact/', views.log_transact, name='logtransact'),
]