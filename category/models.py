from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)	
	
	def __str__(self):
		return self.name
