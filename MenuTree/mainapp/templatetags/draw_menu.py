from django import template

from mainapp.models import Menus

register = template.Library()


@register.inclusion_tag("template_tags/menu.html", takes_context=True)
def draw_menu(context, slug):
    try:
        menu = Menus.objects.get(slug=slug)
        return {"menu": menu, "context": context}
    except Menus.DoesNotExist:
        return {"menu": "", "context": context}
