from django.shortcuts import render

from .models import Menus


# Вывод списка меню
def menu_list(request):
    menu_list = Menus.objects.all().filter(parent__isnull=True)
    content = {"menu_list": menu_list}
    return render(request, "mainapp/index.html", content)


def menu(request, slug):
    menu_tree = Menus.objects.all()
    current_menu = Menus.objects.get(slug=slug)
    content = {"menu_tree": menu_tree, "current_menu": current_menu}
    return render(request, "mainapp/menu.html", content)
