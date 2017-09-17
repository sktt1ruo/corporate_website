from django.conf.urls import url
from online_shop_orders import views

app_name = "online_shop_orders"

urlpatterns = [
    url(r"^$", views.OrderList.as_view(), name="orders"),
    url(r"^(?P<pk>\d+)/$", views.OrderDetail.as_view(), name="order_detail"),
    url(r"^address/$", views.AddressSelectFormView.as_view(), name="order_address"),
    url(r"^address/add/$", views.UserAddressCreateView.as_view(), name="user_address_create"),
    # url(r"^checkout/$", views.CheckoutView.as_view(), name="checkout"),
]