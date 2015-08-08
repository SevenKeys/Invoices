from django import template

register = template.Library()

@register.simple_tag
def add_css_class(css_class):
	return css_class

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})
