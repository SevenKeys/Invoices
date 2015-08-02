from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
from .models import *
from .forms import InvoiceForm
from django.http import HttpResponse
import json
import logging
from django.core import serializers

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
    templates = InvoiceTemplate.objects.filter(company=request.user.userprofile.company).order_by("-created")
    return render_to_response("invoices/templates_list.html", {
        "templates": templates, "user": request.user, "company": request.user.userprofile.company})


def new_template(request):
    defaultcomponents = TemplateComponent.objects.filter(default=True)
    unremovablecomponents = []
    removablecomponents = []
    customcomponents = TemplateComponent.objects.filter(company=request.user.userprofile.company)
    for item in defaultcomponents:
        if item.removable:
            removablecomponents.append(item)
        else:
            unremovablecomponents.append(item)
    return render_to_response("invoices/template_generator.html", {"user": request.user, "defaultcomponents": removablecomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents})


def edit_template(request):
    defaultcomponents = TemplateComponent.objects.filter(default=True)
    unremovablecomponents = []
    removablecomponents = []
    customcomponents = TemplateComponent.objects.filter(company=request.user.userprofile.company)
    template = InvoiceTemplate.objects.get(id=request.GET['id_template'])
    component_instances = TemplateComponentInstance.objects.filter(template=template)
    for item in defaultcomponents:
        if item.removable:
            removablecomponents.append(item)
        else:
            unremovablecomponents.append(item)
    list = []
    for row in component_instances:
        list.append({'id': row.id, 'reference': row.reference, 'position_x': row.position_x, 'position_y': row.position_y, "size_x": row.component.size_x, "size_y": row.component.size_y, "component": row.component.id, "content": row.component.content, "removable": row.component.removable})
    recipe_list_json = json.dumps(list)
    return render_to_response("invoices/template_generator.html", {"user": request.user, "defaultcomponents": removablecomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents, "id_template": template.id, "template": recipe_list_json})


def add_custom_component(request):
    saved_component = TemplateComponent(company=request.user.userprofile.company, default=False, removable=True, title=request.POST['title'], size_x=request.POST['size_x'], size_y=request.POST['size_y'], content=request.POST['content'])
    saved_component.save()
    return HttpResponse(saved_component.id)


def delete_custom_component(request):
    if request.method == 'GET':
        component = TemplateComponent.objects.get(id=request.GET['id_component'])
        instances = TemplateComponentInstance.objects.filter(component=component)
        if instances.exists():
            return HttpResponse("ko")
        else:
            component.delete()
            return HttpResponse("ok")
    else:
        return HttpResponse("ko")


def save_template(request):
    logger = logging.getLogger('challenges.viewset')
    logger.error(request.POST['id_template'])
    if request.POST['id_template'] is "":
        template = InvoiceTemplate(title=request.POST['title_template'], description=request.POST['description_template'], company=request.user.userprofile.company)
        template.save()
    else:
        template = InvoiceTemplate.objects.get(id=request.POST['id_template'])
        TemplateComponentInstance.objects.filter(template=template).delete()
    instances = json.loads(request.POST['instances_template'])
    logger.error(request.POST['instances_template'])
    for instance in instances:
        TemplateComponentInstance(template=template, reference=instance['reference'],
                                  position_x=instance['position_x'], position_y=instance['position_y'],
                                  component=TemplateComponent.objects.get(id=instance['id_component'])).save()

    return HttpResponse(template.id)


class AddInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create_invoice.html'
    success_url = '/invoices/success.html'