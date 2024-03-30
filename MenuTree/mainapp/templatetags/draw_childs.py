from django import template

from mainapp.models import Menus

register = template.Library()


@register.inclusion_tag("template_tags/childs_tag.html", takes_context=True)
def draw_childs(context, parent):
    print(parent)
    try:
        childs = Menus.objects.all().filter(parent__id=parent)
        return {"childs": childs, "context": context}
    except Menus.DoesNotExist:
        print("Не найдены резульатты для отрисовки childs_menu")
        return {"menu": "", "context": context}
