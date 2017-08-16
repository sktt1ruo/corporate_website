from django.conf.urls import url
from online_shop_products import views

app_name = "online_shop_products"

urlpatterns = [
    url(r"^$", views.ProductListView.as_view(), name="products"),
    url(r"^(?P<pk>\d+)/$", views.ProductDetailView.as_view(), name="product_detail"),
    # url(r"^(?P<pk>\d+)/inventory/$", views.VariationListView.as_view(), name="product_inventory"),
    # url(r"^(?P<id>\d+)", views.product_detail_view_func, name="product_detail_function")
]
