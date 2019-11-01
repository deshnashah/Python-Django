from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductForm

# Create your views here.

def products(request):
	context = {
		'products': Products.objects.all()
	}
	return render(request,'Products/productList.html',context)

@login_required
def addProduct(request):
	if request.method == 'POST':
		pr_Form = ProductForm(request.POST)
		if pr_Form.is_valid():
			pr_Form.save()
			name = pr_Form.cleaned_data.get('product_name')
			
			messages.success(request,f'Product has been created successfully! ')
			return redirect('blog-product')
	else:
		pr_Form = ProductForm()
	return render(request,'Products/productForm.html',{'form' : pr_Form})
	
	
@login_required
def editProduct(request,id):
	if request.method == 'GET':
		productDetail = get_object_or_404(Products, id=id)
		pr_form = ProductForm(instance=productDetail)
	elif request.method == 'POST':
		productDetail = get_object_or_404(Products, id=id)
		pr_form = ProductForm(request.POST or None, instance=productDetail)
		if pr_form.is_valid():			
			pr_form.save()
						
			messages.success(request,f'Product has been updated successfully! ')
			return redirect('blog-product')
		else:
			messages.error(request,f'Product Form is not valid')
	else:
		pr_form = ProductForm()
	
	return render(request,'Products/productForm.html',{'form' : pr_form, 'isEdit' : 1})


def deleteProduct(request,id):
	Products.objects.filter(id=id).delete()
	messages.success(request,f'Product deleted successfully! ')
	return redirect('blog-product')
