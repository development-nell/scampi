from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Component
from .forms import ComponentCreate
from django.views.generic import ListView, DetailView

