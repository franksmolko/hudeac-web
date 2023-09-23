from django import template

register = template.Library()

@register.filter
def capital(page):
    return page.capitalize()
    