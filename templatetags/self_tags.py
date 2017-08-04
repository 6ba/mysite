from django import template


register = template.Library()


@register.filter(name="size")
def size(value):
    return len(value)
