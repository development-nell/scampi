from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Component, ProductOption, ProductionQueue, ProductOptionComponent
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

def order(request,product_id,order_number):
    try:
        product = ProductOption.objects.get(id=product_id)
    except Exception as e:
        return JsonResponse({'msg':'Nonexistent SKU dipwad'})
    if(product!=None):
        shortfall = product.produced - order_number
        print(shortfall)
        if (shortfall<=0):

            product.produced =0
            q, created = ProductionQueue.objects.get_or_create(product_option_id=product.id)
            q.units = q.units + abs(shortfall)
            q.save()

        else:
            product.produced = product.produced - order_number
        product.save()
        for component in ProductOptionComponent.objects.filter(product_option_id=product.id):
            component.component.in_stock = component.component.in_stock - (component.units_per*order_number)
            component.component.save()

        component.save()

        return JsonResponse({'msg':'Order queued'})
    else:
        return JsonResponse({'msg':'No product!','error':True})