from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'judul' : "Shop",
        'subJudul' : "Selamat Datang di Bunakit Shop",
        'products' : products,
    }
    return render(request,"shop/index.html",context)


def cart(request):
    context = {
        'judul' : "Shopping Cart",
    }
    return render(request, "shop/shop-cart.html", context)


# ini buat class based view
# class ProductDetailView(DetailView):
#     queryset = Product.objects.all()
#     template_name = "shop/detail.html"


# ini function base view
def detail_view(request, pk=None):
    instance = get_object_or_404(Product, pk=pk)
    #cart_obj,new_obj = Cart.objects.new_or_get(request)
    #print(cart_obj)
    context = {
        'product' : instance,
    #   'cart'    : cart_obj,
    }
    return render(request, "shop/detail.html", context)

def detail_slug_view(request, slug):
    instance = get_object_or_404(Product, slug=slug)
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    print(cart_obj)
    context = {
        'product' : instance, 
        'cart'    : cart_obj,
    }
    return render(request, "shop/detail.html", context)