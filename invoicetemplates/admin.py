from .models import Template, Component, ComponentInstance, ArchetypeElement, Archetype, ArchetypeField
from django.contrib import admin

admin.site.register(Template)
admin.site.register(Component)
admin.site.register(ComponentInstance)
admin.site.register(ArchetypeElement)
admin.site.register(Archetype)
admin.site.register(ArchetypeField)
