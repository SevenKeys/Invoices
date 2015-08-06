from django import template

register = template.Library()

@register.simple_tag
def add_css_class(css_class):
	return css_class
