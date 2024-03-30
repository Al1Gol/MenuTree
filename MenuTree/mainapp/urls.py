from django.urls import path

from mainapp.views import menu, menu_list

app_name = "mainapp"

urlpatterns = [
    path("", menu_list, name="menu_list"),
    path("<slug:slug>/", menu, name="menu"),
]
