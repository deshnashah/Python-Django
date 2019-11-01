from django.db import models
from django.utils import timezone
from category.models import Category

class Products(models.Model):
	STATUS_CHOICES = (        
        ('0','Out Stock'),
        ('1','In Stock'),
        ('2','Running Low'),
    )
    
	product_name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.IntegerField()
	status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=1,
    )
	date_posted = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.product_name
