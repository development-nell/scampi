from django.db import models
from django_mysql import models as mysql_models
import uuid
from django.core.paginator import Paginator

class ComponentCategory(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(ComponentCategory,db_constraint=False,on_delete=models.DO_NOTHING)
    uid = models.CharField(max_length=64, null=False, default="")#uuid.uuid4().hex)
    unit = mysql_models.EnumField(choices=['in', 'mm', 'oz', 'ml','hours','each'], default='each')
    thumbnail=models.ImageField(blank=True,null=True)
    unit_price = models.DecimalField(decimal_places=4,max_digits=10)
    in_stock = models.IntegerField(default=0)
    unit_threshold = models.IntegerField(default=0)
    vendor_url = models.URLField(blank=True,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def inactive(self,page=0):
        return Paginator.page(Component.objects.filter(active=False),page)
    def low(self,page=0):
        return Paginator.page(Component.objects.filter(active=True,in_stock__lte='unit_threshold'))
    def shortfall(self):
        if (self.unit_threshold>0):
            return abs(self.in_stock-self.unit_threshold)
        else:
            return 0
    shortfall.admin_order_field = "shortfall"


class Product(models.Model):
    name = models.CharField(max_length=64)
    uid = models.CharField(max_length=64, null=False, default="")
    unit_price = models.DecimalField(decimal_places=2,max_digits=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductOption(models.Model):
    name=models.CharField(default="default",max_length=32)
    thumbnail = models.ImageField(null=True,blank=True)
    product=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    produced = models.IntegerField(default=0)
    adjustment=models.DecimalField(max_digits=10,decimal_places=2)
    active:models.BooleanField(default=True)

    def __str__(self):

        try:
            return '{} - {} (+${})'.format(self.product.name,self.name,self.adjustment)
        except:
            return "fuck"

class ProductionQueue(models.Model):
    product_option = models.ForeignKey(ProductOption,on_delete=models.CASCADE)
    units = models.IntegerField(default=0)
    status = mysql_models.EnumField(choices=['Pending','In Progress','On Hold'],default="Pending")

    def __str__(self):
        return self.product_option.__str__()

class ProductionLog(models.Model):
    production_queue = models.ForeignKey(ProductionQueue,on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    units_produced = models.IntegerField(default=0)

class ProductOptionComponent(models.Model):
    product_option=models.ForeignKey(to=ProductOption,on_delete=models.CASCADE)
    component=models.ForeignKey(Component,on_delete=models.CASCADE)
    units_per=models.DecimalField(max_digits=10,decimal_places=2,default=1)

    def __str__(self):
        try:
            return "{} {} :{} ".format(self.product_option.product.name,self.product_option.name,self.component.name)
        except Exception as e:
            print(e)
            return "plop"
