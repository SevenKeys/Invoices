from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^invoices/$', 'invoices.views.main'),
                       url(r'^templates/$', 'invoices.views.templates_list'),
                       url(r'^templates/new/$', 'invoices.views.new_template'),
                       url(r'^templates/customcomponents/$', 'invoices.views.add_custom_component'),
                       url(r'^templates/save/$', 'invoices.views.save_template'),
                       url(r'^templates/edit/$', 'invoices.views.edit_template'),
                       url(r'^templates/customcomponents/delete/$', 'invoices.views.delete_custom_component'),
                       url(r'^templates/customcomponents/update/$', 'invoices.views.update_custom_component'),
                       url(r'^templates/get/$', 'invoices.views.get_template'),
                       )
