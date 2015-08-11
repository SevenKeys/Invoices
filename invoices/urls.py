from django.conf.urls import include, url
# from .views import CreateInvoice

urlpatterns = [
    url(r'^$', 'invoices.views.main', name='create_invoice'),
]
