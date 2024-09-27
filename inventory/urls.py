from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_items, name='list_items'),  # This will handle the root URL for the inventory app
    path('add/', views.add_item, name='add_item'),
    path('deduct/<int:item_id>/', views.deduct_item, name='deduct_item'),
]
