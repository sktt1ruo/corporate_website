from django.contrib import admin
from .models import Product, Variation, ProductImage, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 10


class VariatoinInline(admin.TabularInline):
    model = Variation
    extra = 0
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "price"]
    inlines = [
        ProductImageInline,
        VariatoinInline,
    ]

    class Meta:
        model = Product


# Register your models here.
admin.site.register(Product, ProductAdmin)
# admin.site.register(Variation)
# admin.site.register(ProductImage)
admin.site.register(Category)
