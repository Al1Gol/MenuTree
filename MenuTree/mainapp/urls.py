from django.urls import path
from mainapp.views import menu_list

app_name = 'menu_list'

urlpatterns = [
    path('', menu_list, name='menu_list'),
]