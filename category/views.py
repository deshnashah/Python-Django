from django.shortcuts import render
from .models import Category

# Create your views here.

def category(request):
	context = {
		'categories': Category.objects.all()
	}
	return render(request,'category/category.html',context)

