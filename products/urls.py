from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name = 'home'),
    path('product/', views.product_detail,name='product_detail')
]
