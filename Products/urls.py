from django.urls import path
from . import views

urlpatterns = [    
    path('products/', views.products, name='blog-product'),
    path('products/add', views.addProduct, name='product-add'),
    path('products/edit/<int:id>/', views.editProduct, name='product-update'),
    path('products/delete/<int:id>/', views.deleteProduct, name='product-delete'),
]
