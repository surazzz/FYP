from django.contrib import admin
from commerce.models import Product, Category, Blog, Addtocart, Cartdetail, Address, Contactus

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Addtocart)
admin.site.register(Cartdetail)
admin.site.register(Address)
admin.site.register(Contactus)