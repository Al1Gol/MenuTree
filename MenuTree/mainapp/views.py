from django.shortcuts import render
from .models import Menus

# Вывод списка меню
def menu_list(request):
    menu_list = Menus.objects.all()
    content = {
        'menu_list': menu_list,
    }
    return render(request, "mainapp/index.html", content)