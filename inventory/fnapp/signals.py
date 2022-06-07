from urllib import request
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:    
        req_obj = Student(first_name = instance.first_name, last_name = instance.last_name, email_id = instance.email)
        req_obj.save()
