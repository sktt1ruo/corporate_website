from django.conf.urls import url
from online_shop_products import views

app_name = "online_shop_categories"

urlpatterns = [
    url(r"^$", views.CategoryListView.as_view(), name="categories"),
    url(r"^(?P<slug>[\w-]+)/$", views.CategoryDetailView.as_view(), name="category_detail"),
]
