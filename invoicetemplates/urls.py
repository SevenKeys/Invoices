from django.conf.urls import include, url
# from .views import CreateInvoice

urlpatterns = [
    url(r'^$', 'invoicetemplates.views.templates_list', name='templates_list'),
    url(r'^new/$', 'invoicetemplates.views.new_template', name='new_template'),
    url(r'^edit$', 'invoicetemplates.views.edit_template', name='edit_template'),
    url(r'^customcomponents/$', 'invoicetemplates.views.add_custom_component', name='add_custom_component'),
    url(r'^get/$', 'invoicetemplates.views.get_template', name='get_template'),
    url(r'^customcomponents/update/$', 'invoicetemplates.views.update_custom_component', name='update_custom_component'),
    url(r'^customcomponents/delete/$', 'invoicetemplates.views.delete_custom_component', name='delete_custom_component'),
    url(r'^save/$', 'invoicetemplates.views.save_template', name='save_template'),
    url(r'^preview/$', 'invoicetemplates.views.print_preview', name='print_preview')
]