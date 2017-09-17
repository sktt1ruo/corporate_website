from django.conf.urls import url
from online_shop_carts import views

app_name = "online_shop_carts"

urlpatterns = [
    url(r"^$", views.CartView.as_view(), name="cart"),
    url(r"^count/$", views.ItemCountView.as_view(), name="item_count"),
    url(r"^checkout/$", views.CheckoutView.as_view(), name="checkout"),
    url(r"^checkout/final/$", views.CheckoutFinalView.as_view(), name="checkout_final"),
]
