from django.contrib import admin
from .models import Component,ProductOption,Product,ProductOptionComponent
# Register your models here.

admin.site.register(Component)
admin.site.register(Product)
admin.site.register(ProductOption)
admin.site.register(ProductOptionComponent)
