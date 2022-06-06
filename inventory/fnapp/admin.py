from django.contrib import admin
# Register your models here.
from .models import Item, Through, Student
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.

admin.site.register(Item)
admin.site.register(Through)
admin.site.register(Student)

