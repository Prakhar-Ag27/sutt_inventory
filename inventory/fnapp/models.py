import email
from urllib import request
from django.db import models
from django.contrib.auth.models import User
import random

class Item(models.Model):
    type_of_item = models.CharField(max_length=20)
    name_of_item = models.CharField(max_length=20)
    total_qty = models.IntegerField(default=0)
    current_out = models.IntegerField(default=0)
    unique_code = models.IntegerField(default=random.randint(10_000_000, 99_999_999), editable = False)
    added_on = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
        return self.name_of_item

class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + self.last_name

class Through(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    qty_issued = models.IntegerField(default = 0)
    time_of_issue = models.DateTimeField(null = True, editable = False)
    time_of_return = models.DateTimeField(null = True, editable = False)
    time_of_issue_int = models.IntegerField(null = True)
    qty_returned = models.IntegerField(default = 0)
    current_issued = models.IntegerField(default = 0)
    is_returned = models.BooleanField(default = False)

    def save(self,*args, **kwargs):
        if self.qty_issued == self.qty_returned:
            self.is_returned = True
        super().save(*args, **kwargs)      