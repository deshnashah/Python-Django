from django.urls import path
from . import views

urlpatterns = [    
    path('category/', views.category, name='blog-category'),
    path('category/add/', views.addCategory, name='category-add'),
    path('category/edit/<int:id>/', views.editCategory, name='category-update'),
    path('category/delete/<int:id>/', views.deleteCategory, name='category-delete'),
]
