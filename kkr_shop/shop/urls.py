from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),  # List of all stores
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),  # Store detail page
]