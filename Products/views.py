from django.shortcuts import render
from .models import Products

# Create your views here.

def products(request):
	context = {
		'products': Products.objects.all()
	}
	return render(request,'Products/productList.html',context)

