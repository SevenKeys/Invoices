from django.views.generic.edit import CreateView
from .models import *
from .forms import InvoiceForm


class AddInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create_invoice.html'
    success_url = '/invoices/success.html'