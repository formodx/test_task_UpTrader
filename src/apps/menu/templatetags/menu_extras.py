from django.template import Library

from apps.menu.models import Menu


register = Library()

@register.inclusion_tag('tags/menu.html')
def draw_menu(name, count=0):
    count += 30

    return {'root': Menu.objects.get(name=name), 'count': count}