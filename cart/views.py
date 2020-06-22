from django.shortcuts import render, redirect
from shop.models import Product
from .models import Cart

def cart_home(request):
    # logic nya sudah dibuat sebagai Models Manager di models.py 
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    context = {
        "cart" : cart_obj
    }

    return render(request, "cart/home.html", context)

def cart_update(request):
    #print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Message for user, product not found")
            redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['total_cart_item'] = cart_obj.products.count()

    return redirect("cart:home")