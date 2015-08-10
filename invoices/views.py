from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response

from .models import *


def main(request):
    """Main listing."""
    invoices = Invoice.objects.all().order_by("-created")
    paginator = Paginator(invoices, 2)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        invoices = paginator.page(page)
    except (InvalidPage, EmptyPage):
        invoices = paginator.page(paginator.num_pages)

    return render_to_response("invoices/list.html", dict(invoices=invoices, user=request.user,
                                                invoices_list=invoices.object_list))
