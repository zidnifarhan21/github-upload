from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

# ini views buat auth milik django
from django.contrib.auth import views as auth_views 

from . import views

app_name = 'ecomm'
    
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^login-page/', views.login),
    url(r'^cart/', include("cart.urls", namespace='cart')),
    url(r'^shop/', include("shop.urls", namespace='shop')),
    url(r'^oauth/', include("social_django.urls", namespace='social')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/', include("accounts.urls", namespace='accounts')),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="index.html"), name="logout"),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #backup url
    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^login/$', auth_views.login, name='login'),