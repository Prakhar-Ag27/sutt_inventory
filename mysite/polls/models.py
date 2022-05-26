from django.db import models

class Questions(models.Model):
	question_text = models.CharField(max_length = 777)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Questions, on_delete = models.CASCADE)
	votes = models.IntegerField(default=0)