from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html,format_html_join
from django.utils.safestring import mark_safe
from django.db.models import F
from .models import Component, ProductOption, Product, ProductOptionComponent, ComponentCategory, ProductionQueue


# Register your models here.


class ProductOptionComponentsInline(admin.StackedInline):
    model = ProductOptionComponent
    extra = 0

class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ['label','produced']
    fields=['name','product','adjustment','produced']
    search_fields = ['name']
    save_as = True

    inlines = [ProductOptionComponentsInline]
    def label(self,instance):
        return '{} - {} '.format(instance.product.name,instance.name)
class ProductOptionsInline(admin.StackedInline):
    admin =ProductOptionAdmin
    model = ProductOption
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    fields = ['name','unit_price','options','options_link']
   # inlines = [ProductOptionsInline]
    readonly_fields = ('options_link','options')
    list_display = ["name","unit_price","options_link"]
    save_as = True
    def options(self,instance):
        existing = ProductOption.objects.filter(product_id=instance.id)
        if (existing.count()>0):
            return mark_safe("<ul>")+format_html_join(mark_safe('<li>'),'<a href="/admin/main/productoption/{}/change">{}</a>',((option.id,option.name) for option in existing))+mark_safe('</ul>')
        else:
            return ""


    def options_link(self, instance):
        # assuming get_full_address()
        return format_html('<a href="/admin/main/productoption/?product={}">Options</a>',instance.id)
    options_link.short_description = "Edit Options"

class LowInventoryFilter(SimpleListFilter):

    title = 'Low Inventory'
    parameter_name = 'low'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Low'),
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == '1':
            return queryset.filter(in_stock__lt=F('unit_threshold'),unit_threshold__gt=1)
        else:
            return queryset
        #     return queryset.filter().exclude(user__email__regex=self.SOCIAL_EMAIL_REGEX)

class ComponentAdmin(admin.ModelAdmin):
    fields = ['name','category','unit','thumbnail','unit_price','in_stock','unit_threshold']
    list_filter = [LowInventoryFilter]
    list_display = ['displayname','in_stock','shortfall']
    def displayname(self,instance):
        return '{}'.format(instance.__str__())
    def shortfall(self,instance):
        return instance.shortfall()
    save_as = True

    displayname.short_description="Name"


class ComponentCategoryAdmin(admin.ModelAdmin):
    fields = ['name']


class ProductionQueueAdmin(admin.ModelAdmin):
    list_display = ['displayname','units']
    def displayname(self,instance):
        return instance.product_option.__str__()

    def get_ordering(self,request):
       return ['-units']

admin.site.register(Product,ProductAdmin)
admin.site.register(Component,ComponentAdmin)
admin.site.register(ProductOption,ProductOptionAdmin)
admin.site.register(ProductOptionComponent)
admin.site.register(ComponentCategory,ComponentCategoryAdmin)
admin.site.register(ProductionQueue,ProductionQueueAdmin)