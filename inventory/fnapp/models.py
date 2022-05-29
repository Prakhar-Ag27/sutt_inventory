from django.db import models
from django.utils import timezone
import random

class items(models.Model):
    type_of_item = models.CharField(max_length=50)
    name_of_item = models.CharField(max_length=50)
    qty_available = models.IntegerField(default = 0)
    last_issued = models.DateTimeField()
    no_of_items_issued_out = models.IntegerField(default = 0)
    unique_code = models.IntegerField(max_length=100, default = random.randint(10_000_000, 99_999_999), editable = False)
    

    def __str__(self):
        return self.name_of_item


    