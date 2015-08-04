from django.conf.urls import include, url
# from .views import CreateInvoice

# urlpatterns = patterns('invoices.views',
                       # (r"", "main"),
                       # )
urlpatterns = [
	url(r'^$', 'invoices.views.main', name='create_invoice'),
	# url(r'^create/$', CreateInvoice.as_view(), name='create_invoice')
]