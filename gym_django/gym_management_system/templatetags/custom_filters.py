from django import template

register = template.Library()

@register.filter(name='break_loop')
def break_loop(value):
    raise StopIteration

break_loop.is_safe = True