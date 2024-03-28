from django import template

from mainapp.models import Menus

register = template.Library()


@register.inclusion_tag("template_tags/child_menu.html", takes_context=True)
def components_menu(context, item):
    childs = Menus.objects.all()
    return {"item": item, "childs": childs}
