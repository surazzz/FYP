from django.contrib import admin
from commerce.models import Product, Category, Blog, addtocart, cartdetail

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(addtocart)
admin.site.register(cartdetail)