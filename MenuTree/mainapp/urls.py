from django.urls import path, re_path

from mainapp.views import menu, menu_list

app_name = "mainapp"

urlpatterns = [
    re_path(r"^$", menu_list, name="menu_list"),
    re_path(r"^[\dA-Za-z_/-]+", menu, name="menu"),
]
