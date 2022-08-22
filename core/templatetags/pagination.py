from django import template
register = template.Library()


@register.simple_tag
def update_page_number_in_url(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
