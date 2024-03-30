from django import template

from mainapp.models import Menus

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, path):
    if path in context.request.get_full_path():
        return "active"
    else:
        return None


@register.inclusion_tag("template_tags/menu_tag.html", takes_context=True)
def draw_menu(context, slug):
    slug = slug[1:-1]
    print(context.request.get_full_path())
    try:
        menu = Menus.objects.get(slug=slug)
        childs = Menus.objects.all().filter(parent=menu.id)
        return {"menu": menu, "childs": childs, "context": context}
    except Menus.DoesNotExist:
        print("Не найдены резульатты для отрисовки draw_menu")
        return {"menu": "", "context": context}
