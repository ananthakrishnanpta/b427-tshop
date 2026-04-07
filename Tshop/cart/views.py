from django.shortcuts import render

from .models import CartItem

# Create your views here.
from django.views.generic import TemplateView, ListView



class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'cart_items'

# def view_cart(request):
#     context = {
#         'cart_items' : CartItem.objects.filter(user = request.user)
#         }
#     template_name = 'cart/cart.html'
#     return render(request, template_name, context)
