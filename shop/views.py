from django.shortcuts import render
from .models import Item, Order, OrderItem


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "item_list.html", context)
