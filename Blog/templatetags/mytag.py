



from django import template

register = template.Library()

@register.inclusion_tag('tags/search.html')
def search():
    pass
