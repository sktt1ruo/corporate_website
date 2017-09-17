"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from online_shop_carts.views import CartView, ItemCountView, CheckoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^buy/', include('buy.urls')),

    url(r"^online_shop_products/", include("online_shop_products.urls")),
    url(r"^online_shop_categories/", include("online_shop_products.urls_categories")),
    url(r"^online_shop_cart/", include("online_shop_carts.urls")),
    url(r"^online_shop_orders/", include("online_shop_orders.urls")),

    # url(r"^cart/$", CartView.as_view(), name="cart"),
    # url(r"^cart/count/$", ItemCountView.as_view(), name="item_count"),
    # url(r"^checkout/$", CheckoutView.as_view(), name="checkout"),

    url(r'^accounts/', include('registration.backends.hmac.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
