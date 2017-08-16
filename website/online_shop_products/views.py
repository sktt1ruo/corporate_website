from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
import random


from .models import Product, Category


# class VariationListView(ListView):
#     model = Variation
#
#     def get_queryset(self, *args, **kwargs):
#         product_pk = self.kwargs.get("pk")
#         if product_pk:
#             product = get_object_or_404(Product, pk=product_pk)
#             queryset = Variation.objects.filter(product=product)
#         return queryset


class CategoryListView(ListView):
    model = Category
    template_name = "online_shop_products/product_list.html"


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.product_set.all()
        default_products = obj.default_category.all()
        products = (product_set | default_products).distinct()
        context["products"] = products
        return context


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context["related"] = sorted(Product.objects.get_related(instance)[:3], key=lambda x: random.random())
        return context


def product_detail_view_func(request, id):
    # product_instance = Product.objects.get(id=id)
    product_instance = get_object_or_404(Product, id=id)
    template = "online_shop_products/product_detail.html"
    context = {
        "object": product_instance
    }
    return render(request, template, context)
