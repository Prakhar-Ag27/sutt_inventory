import email
from django.db import models
from django.utils import timezone
import random

class items(models.Model):
    type_of_item = models.CharField(max_length=50)
    name_of_item = models.CharField(max_length=50)
    qty_available = models.IntegerField(default = 0)
    last_issued = models.DateTimeField()
    no_of_items_issued_out = models.IntegerField(default = 0)
    unique_code = models.IntegerField(default = random.randint(10_000_000, 99_999_999), editable = False)
    added_on = models.DateTimeField(auto_now_add = True, editable = False)
    

    def __str__(self):
        return self.name_of_item

class issue_items(models.Model):
    username_of_borrower = models.CharField(max_length=50)
    email_of_borrower = models.EmailField(max_length=254)
    borrowed_item_code =  models.IntegerField(default=0)
    time_of_issue = models.DateTimeField(auto_now= True, editable = False)



    