from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Item, Order, OrderItem


class HomeView(ListView):
    model = Item
    template_name = "item_list.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "This item quantity was updated.")
            return redirect("shop:product", slug=slug)
        else:
            messages.success(request, "This item was added to the cart.")
            order.items.add(order_item)
            return redirect("shop:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, "This item was added to the cart")
        return redirect("shop:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from the cart.")
            return redirect("shop:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("shop:product", slug=slug)
    else:
        # add a message saying user don't have an order
        messages.info(request, "You do not have an active order.")
        return redirect("shop:product", slug=slug)
