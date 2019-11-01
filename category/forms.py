from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(label='Category name', max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
	
	class Meta:
		model = Category
		fields = ['name','description']
