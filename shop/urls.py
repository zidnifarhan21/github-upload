# INI URLS MILIK SHOP

from django.urls import include
from django.conf.urls import url

from . import views

app_name="shop"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view()),    #ini buat class based view
    url(r'^product/(?P<pk>\d+)/$', views.detail_view),
    url(r'^product/(?P<slug>[\w-]+)/$', views.detail_slug_view),
    url(r'^cart$', views.cart, name="cart"),
]
