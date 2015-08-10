from django.conf.urls import include, url
# from .views import CreateInvoice

# urlpatterns = patterns('invoices.views',
                       # (r"", "main"),
                       # )
urlpatterns = [
	url(r'^templates/$', 'invoices.views.templates_list', name='templates_list'),
	url(r'^templates/new/$', 'invoices.views.new_template', name='new_template'),
	url(r'^templates/edit$', 'invoices.views.edit_template', name='edit_template'),
	url(r'^templates/customcomponents/$', 'invoices.views.add_custom_component', name='add_custom_component'),
	url(r'^templates/get/$', 'invoices.views.get_template', name='get_template'),
	url(r'^templates/customcomponents/update/$', 'invoices.views.update_custom_component', name='update_custom_component'),
	url(r'^templates/customcomponents/delete/$', 'invoices.views.delete_custom_component', name='delete_custom_component'),
	url(r'^templates/save/$', 'invoices.views.save_template', name='save_template'),
	url(r'^templates/preview/$', 'invoices.views.print_preview', name='print_preview'),
	# url(r'^create/$', CreateInvoice.as_view(), name='create_invoice')
]