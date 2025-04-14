from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def personal(request):
    return render(request, 'dashboard/personal.html')

def productos(request):
    return render(request, 'dashboard/productos.html')

def ordenes(request):
    return render(request, 'dashboard/ordenes.html')
