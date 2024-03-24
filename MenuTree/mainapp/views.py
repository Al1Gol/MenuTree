from django.shortcuts import render

from .models import Menus


# Вывод списка меню
def menu_list(request):
    menu_list = Menus.objects.all().filter(parent__isnull=True)
    content = {"menu_list": menu_list}
    return render(request, "mainapp/index.html", content)


def menu(request, menu):
    content = {"menu": menu}
    return render(request, "mainapp/menu.html", content)
