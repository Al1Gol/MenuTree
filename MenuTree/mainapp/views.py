from django.shortcuts import render
from .models import Menus

# Create your views here.
def request():
    menu_list = Menus.objects.get()
    content = {
        'menu_list': menu_list 
    }
    return render(request, "mainapp/products.html", content)