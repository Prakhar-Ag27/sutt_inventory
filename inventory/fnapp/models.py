import email
from urllib import request
from django.db import models
from django.utils import timezone
import random

###class items(models.Model):
###  name_of_item = models.CharField(max_length=50)
###    qty_available = models.IntegerField(default = 0)
###    last_issued = models.DateTimeField()
 ###   no_of_items_issued_out = models.IntegerField(default = 0)
 ###   unique_code = models.IntegerField(default = random.randint(10_000_000, 99_999_999), editable = False)
 ###   added_on = models.DateTimeField(auto_now_add = True, editable = False)
###    
 ###   def __str__(self):
 ###       return self.name_of_item

###class issue_items(models.Model):
 ###   username_of_borrower = models.CharField(max_length=50)
###    email_of_borrower = models.EmailField(max_length=254)
 ###   borrowed_item_code =  models.IntegerField(default=0)
 ###   time_of_issue = models.DateTimeField(auto_now= True, editable = False)

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
    first_name = models.CharField(max_length=15, editable = False)
    last_name = models.CharField(max_length=15, editable = False)
    email_id = models.EmailField(max_length=254, editable = False)

    def __str__(self):
        return self.first_name + self.last_name

class Through(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    qty_issued = models.IntegerField(default = 1)
    time_of_issue = models.DateTimeField(auto_now_add = True, editable = False)
    time_of_return = models.DateTimeField(auto_now_add = True, editable = False)
    qty_returned = models.IntegerField(default = 0)
    is_returned = models.BooleanField(default = False)

    def save(self,*args, **kwargs):
        if self.qty_issued == self.qty_returned:
            self.is_returned = True
        super().save(*args, **kwargs)  
  
        



    