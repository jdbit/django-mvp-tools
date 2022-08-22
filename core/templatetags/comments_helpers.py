from django import template
register = template.Library()


@register.simple_tag
def indent_comment(value):
    return value
