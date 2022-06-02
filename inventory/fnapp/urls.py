from django.urls import path

from . import views

app_name = 'fnapp'
urlpatterns = [
    path('', views.details, name='details'),
    path('<int:itemcode>/', views.issue, name='issue'),
    path('success/<int:itemcode>/<int:temp>', views.success_return, name='success_return'),
    path('success/<int:itemcode>/', views.success_issue, name='success_issue'),
    path('logadd/', views.log_add, name='logadd'),
    path('logissue/', views.log_issue, name='logissue'),
    path('logreturn/', views.log_return, name='logreturn'),
    path('returnitems/', views.returnitems, name='returnitems'),
]