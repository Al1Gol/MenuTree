from django.urls import path

from mainapp.views import menu, menu_list

app_name = "mainapp"

urlpatterns = [
    path("", menu_list, name="menu_list"),
    path("<slug:post_slug>", menu, name="menu"),
]
