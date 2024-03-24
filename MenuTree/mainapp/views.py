from django.shortcuts import render

from .models import Elements, Menus


# Вывод списка меню
def menu_list(request):
    menu_list = Menus.objects.all()
    parents = Elements.objects.all()
    content = {"menu_list": menu_list, "parents": parents}
    return render(request, "mainapp/index.html", content)
