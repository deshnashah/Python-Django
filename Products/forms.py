from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
	#name = forms.CharField(label='Product name', max_length=200)
	
	
	class Meta:
		model = Products
		fields = "__all__"
