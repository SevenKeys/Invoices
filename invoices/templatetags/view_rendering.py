# little hack to have the definition in common but ability to use it everywhere
from django.template import Library

from common.templatetags.view_rendering import do_view

register = Library()
register.tag('view', do_view)
