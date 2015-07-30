from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^invoices/$', 'invoices.views.main'),
                       url(r'^templates/$', 'invoices.views.templates_list'),
                       url(r'^templates/new/$', 'invoices.views.new_template'),
                       url(r'^templates/customcomponents/new/$', 'invoices.views.add_custom_component'),
                       )
