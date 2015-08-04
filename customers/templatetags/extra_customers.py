from django import template

register = template.Library()

@register.filter
def fieldtype(obj):
	return obj.__class__.__name__


@register.simple_tag
def add_css_class(css_class):
	return css_class