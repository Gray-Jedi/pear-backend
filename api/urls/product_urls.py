from django.urls import path 
from api.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name="products"),
    path('create/', views.createProduct, name="product-create"),
    path('<str:pk>/', views.getProduct, name="product"),
    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    # path('top/', views.getTopProducts, name='top-products'),
    path('upload/', views.uploadImage, name="image-upload"),
    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
]
    
    

