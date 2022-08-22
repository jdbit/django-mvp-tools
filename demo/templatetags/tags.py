from django import template
from demo.models import Post
register = template.Library()


@register.inclusion_tag('snippets/tags.html')
def popular_tags(obj, amount):
    tags = type(obj).tags.most_common()[:amount]
    return {'tags': tags}
