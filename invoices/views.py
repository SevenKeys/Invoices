from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
from .models import *
from .forms import InvoiceForm
from django.http import HttpResponse


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


def templates_list(request):
    my_company = request.user.userprofile.company
    if my_company is None:
        templates = InvoiceTemplate.objects.filter(company=request.user.userprofile.company).order_by("-created")
    else:
        templates = None
    return render_to_response("invoices/templates_list.html", {
        "templates": templates, "user": request.user, "company": my_company})


def new_template(request):
    defaultcomponents = TemplateComponent.objects.filter(default=True)
    unremovablecomponents = []
    customcomponents = TemplateComponent.objects.filter(company=request.user.userprofile.company)
    for item in defaultcomponents:
        if not item.removable:
            unremovablecomponents.append(item)
    return render_to_response("invoices/template_generator.html", {"user": request.user, "defaultcomponents": defaultcomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents})


def add_custom_component(request):
    saved_component = TemplateComponent(company=request.user.userprofile.company, default=False, removable=False, title=request.POST['title'], size_x=request.POST['size_x'], size_y=request.POST['size_y'], content=request.POST['content'])
    saved_component.save()
    return HttpResponse(saved_component.id)


class AddInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create_invoice.html'
    success_url = '/invoices/success.html'