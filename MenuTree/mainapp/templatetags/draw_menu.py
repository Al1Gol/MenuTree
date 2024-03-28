from django import template

from mainapp.models import Menus

register = template.Library()


@register.inclusion_tag("template_tags/menu_tag.html", takes_context=True)
def draw_menu(context, slug):
    slug = slug[1:-1]
    try:
        menu = Menus.objects.get(slug=slug)
        childs = Menus.objects.all().filter(parent=menu.id)
        return {"menu": menu, "childs": childs, "context": context}
    except Menus.DoesNotExist:
        print("Не найдены резульатты для отрисовки draw_menu")
        return {"menu": "", "context": context}
