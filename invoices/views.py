from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
from .models import *
from .forms import InvoiceForm
from django.http import HttpResponse
import json
from io import BytesIO
from reportlab.platypus import Paragraph, Frame, BaseDocTemplate, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import logging

size = A4
styles = getSampleStyleSheet()


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
    for item in defaultcomponents:
        if item.removable:
            removablecomponents.append(item)
        else:
            unremovablecomponents.append(item)
    return render_to_response("invoices/template_generator.html", {"user": request.user, "defaultcomponents": removablecomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents, "id_template": template.id, "title_template": template.title, "description_template": template.description})


def get_template(request):
    template = InvoiceTemplate.objects.get(id=request.GET['id_template'])
    component_instances = TemplateComponentInstance.objects.filter(template=template)
    list = []
    for row in component_instances:
        list.append({'id': row.id, 'reference': row.reference, 'position_x': row.position_x, 'position_y': row.position_y, "size_x": row.component.size_x, "size_y": row.component.size_y, "component": row.component.id, "content": row.component.content, "removable": row.component.removable})
    return HttpResponse(json.dumps(list), content_type="application/json")


def add_custom_component(request):
    saved_component = TemplateComponent(company=request.user.userprofile.company, default=False, removable=True, title=request.POST['title'], size_x=request.POST['size_x'], size_y=request.POST['size_y'], content=request.POST['content'])
    saved_component.save()
    return HttpResponse(saved_component.id)


def update_custom_component(request):
    TemplateComponent.objects.filter(pk=request.POST['id_component']).update(title=request.POST['title'], content=request.POST['content'])
    return HttpResponse(request.POST['id_component'])


def delete_custom_component(request):
    if request.method == 'GET':
        component = TemplateComponent.objects.get(id=request.GET['id_component'])
        instances = TemplateComponentInstance.objects.filter(component=component)
        if instances.exists():
            return HttpResponse("ko")
        else:
            component.delete()
            return HttpResponse("ok", content_type="application/json")
    else:
        return HttpResponse("ko")


def save_template(request):
    if request.POST['id_template'] is "":
        template = InvoiceTemplate(title=request.POST['title_template'], description=request.POST['description_template'], company=request.user.userprofile.company)
        template.save()
    else:
        template = InvoiceTemplate.objects.get(id=request.POST['id_template'])
        TemplateComponentInstance.objects.filter(template=template).delete()
        InvoiceTemplate.objects.filter(id=request.POST['id_template']).update(title=request.POST['title_template'], description=request.POST['description_template'])
    instances = json.loads(request.POST['instances_template'])
    for instance in instances:
        TemplateComponentInstance(template=template, reference=instance['reference'],
                                  position_x=instance['position_x'], position_y=instance['position_y'],
                                  component=TemplateComponent.objects.get(id=instance['id_component'])).save()

    return HttpResponse(template.id)


def print_preview(request):
    components = json.loads(request.GET['instances_template'])
    logger = logging.getLogger("eoeoeoe")
    header_list = header_content(components)
    footer_list = footer_content(components)

    def footer_repeat(canvas, doc):
        canvas.saveState()
        for item in header_list:
            Frame(item['position_x']*inch, size[1] - item['position_y']*inch, item['size_x']*inch, item['size_y']*inch).\
                addFromList([Paragraph(TemplateComponent.objects.get(id=item['id_component']).content, styles['Normal'])], canvas)
        for footer_item in footer_list:
            Frame(footer_item['position_x']*inch, size[1] - footer_item['position_y']*inch, footer_item['size_x']*inch, footer_item['size_y']*inch).\
                addFromList([Paragraph(TemplateComponent.objects.get(id=footer_item['id_component']).content, styles['Normal'])], canvas)
        canvas.restoreState()
    output = BytesIO()
    doc = BaseDocTemplate(output, pagesize=size)
    limit_header = 0
    size_header = 0
    limit_footer = 100000
    for element in header_list:
        if element['position_y'] > limit_header:
            limit_header = element['position_y']
            size_header = element['size_x']
    for element in footer_list:
        if element['position_y'] < limit_footer:
            limit_footer = element['position_y']
    doc.addPageTemplates([PageTemplate(id="test", frames=Frame(doc.leftMargin, size[1] - (limit_header + size_header)*inch, doc.width, 1*inch), onPage=footer_repeat)])
    story = []
    for i in range(100):
        story.append(Paragraph("<font color='blue'> Ey you</font><br/>Youtoo", styles['Normal']))
    doc.build(story)
    pdf_output = output.getvalue()
    output.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    response.write(pdf_output)
    return response


def header_content(components):
    header = []
    center_element = 1
    for entity in components:
        if entity['id_component'] == 1:
            center_element = entity['position_y']

    for entity in components:
        if entity['position_y'] < center_element:
            header.append(entity)
    return header


def footer_content(components):
    footer = []
    center_element = 1
    for entity in components:
        if entity['id_component'] == 1:
            center_element = entity['position_y']

    for entity in components:
        if entity['position_y'] > center_element:
            footer.append(entity)
    return footer


class AddInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create_invoice.html'
    success_url = '/invoices/success.html'