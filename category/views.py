from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm

# Create your views here.

def category(request):
	context = {
		'categories': Category.objects.all()
	}
	return render(request,'category/category.html',context)

@login_required
def addCategory(request):
	if request.method == 'POST':
		cat_Form = CategoryForm(request.POST)
		if cat_Form.is_valid():
			cat_Form.save()
			name = cat_Form.cleaned_data.get('name')
			description = cat_Form.cleaned_data.get('description')
			
			messages.success(request,f'Category has been created successfully! ')
			return redirect('blog-category')
	else:
		cat_Form = CategoryForm()
	return render(request,'category/categoryForm.html',{'form' : cat_Form})


@login_required
def editCategory(request,id):
	categoryDetail = {}
	if request.method == 'GET':		
		categoryDetail = Category.objects.get(id=id)
		cat_Form = CategoryForm(instance=categoryDetail)
	elif request.method == 'POST':	
		instance = get_object_or_404(Category, id=id)
		cat_Form = CategoryForm(request.POST or None, instance=instance)
		
		if cat_Form.is_valid():			
			cat_Form.save()
			name = cat_Form.cleaned_data.get('name')
			description = cat_Form.cleaned_data.get('description')
			
			messages.success(request,f'Category has been updated successfully! ')
			return redirect('blog-category')
		else:
			messages.error(request,f'Form is not valid')
	else:		
		cat_Form = CategoryForm()
		
	return render(request,'category/categoryForm.html',{'form' : cat_Form, 'isEdit': '1', 'category': categoryDetail})


@login_required
def deleteCategory(request,id):	
	Category.objects.filter(id=id).delete()
	messages.success(request,f'Category deleted successfully! ')
	return redirect('blog-category')
