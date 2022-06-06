from django.urls import path

from . import views

app_name = 'fnapp'
urlpatterns = [
    path('', views.details, name='details'),
    path('<int:itemcode>/', views.issue, name='issue'),
    path('success/<int:itemcode>/<int:temp>/<int:timeofissueint>/', views.success_return, name='success_return'),
    path('success/<int:itemcode>/', views.success_issue, name='success_issue'),
    path('logadd/', views.log_add, name='logadd'),
    path('logissue/', views.log_issue, name='logissue'),
    path('logreturn/', views.log_return, name='logreturn'),
    path('returnitems/', views.return_items, name='returnitems'),
    path('edititem/', views.edit_item, name='edititem'),
    path('editpage/<int:itemcode>/', views.edit_item_two, name='edititemtwo'),
    path('editsuccess/<int:itemcode>/', views.edit_item_three, name='edititemthree'),
    path('filter/', views.filter, name='filter'),
    path('upload/', views.simple_upload, name='upload'),
    path('successupload/', views.success_upload, name='success_upload'),
    
]