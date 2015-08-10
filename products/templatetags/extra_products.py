from django import template

register = template.Library()


@register.filter
def fieldtype(obj):
    return obj.__class__.__name__


@register.simple_tag
def add_css_class(css_class):
    return css_class


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='addattr')
def addattr(field, attr):
    return field.as_widget(attrs={"style": attr})
