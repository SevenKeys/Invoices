# little hack to have the definition in common but ability to use it everywhere
from common.templatetags.view_rendering import do_view
from django.template import Library

register = Library()
register.tag('view', do_view)
