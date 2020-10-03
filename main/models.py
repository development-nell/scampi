from django.db import models
from django_mysql import models as mysql_models
import uuid
from django.core.paginator import Paginator


# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=64)
    sku = models.CharField(max_length=64, null=True, default=uuid.uuid4().hex),
    unit = mysql_models.EnumField(choices=['in', 'mm', 'oz', 'ml', 'each'], default='each')
    thumbnail=models.ImageField(null=True)
    unit_price = models.DecimalField(decimal_places=2,max_digits=10)
    in_stock = models.IntegerField(default=0)
    unit_threshold = models.IntegerField(default=0)
    vendor_url = models.URLField(null=True)
    active = models.BooleanField(default=True)

    def inactive(self,page=0):
        return Paginator.page(Component.objects.filter(active=False),page)
    def low(self,page=0):
        return Paginator.page(Component.objects.filter(active=True,in_stock__lte='unit_threshold'))

