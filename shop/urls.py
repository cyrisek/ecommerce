from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeView.as_view(), name='item-list'),
    path('product/<slug>', views.ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>', views.remove_from_cart, name='remove_from_cart'),
]
