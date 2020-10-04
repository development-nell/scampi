from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('order_queue/<int:product_id>/<int:order_number>', views.order, name='order_queue'),
]