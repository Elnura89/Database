from django.shortcuts import render
from .models import *
import os

# Create your views here.
def index(request):
    rows = Students.objects.all()
    context = {
        'rows': rows
    }
    return render (request, 'index.html', context)