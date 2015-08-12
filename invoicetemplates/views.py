from django.shortcuts import render_to_response
from .models import *
from django.http import HttpResponse
import json
from io import BytesIO
from reportlab.platypus import Frame, BaseDocTemplate, PageTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import logging
from .helpers import Pdf, IMAGE, IMAGES_BASE, LOGO, IMAGE_1, SIZE_Y, SIZE_X, LOGO_EXAMPLE, CONTENT, COMPONENT, Y, X, REFERENCE

logger = logging.getLogger("main.views.invoicetemplates")
size = A4
styles = getSampleStyleSheet()
LIST = "invoicetemplates/templates_list.html"
EDIT_TEMPLATE = "invoicetemplates/template_generator.html"
ID_TEMPLATE = "id_template"
COMPONENTS = "instances_template"
DESC_TEMPLATE = "description_template"


def templates_list(request):
    templates = InvoiceTemplate.objects.filter(company=request.user.userprofile.company).order_by("-created")
    return render_to_response(LIST, {
        "templates": templates, "user": request.user, "company": request.user.userprofile.company})


def new_template(request):
    defaultcomponents = TemplateComponent.objects.filter(default=True)
    unremovablecomponents = []
    removablecomponents = []
    customcomponents = TemplateComponent.objects.filter(company=request.user.userprofile.company)
    for item in defaultcomponents:
        if item.type == IMAGE:
            item.content = item.content.replace("[url]", "/" + IMAGES_BASE + "/" + IMAGE_1)
        elif item.type == LOGO:
            item.content = item.content.replace("[url]", "/" + IMAGES_BASE + "/" + LOGO_EXAMPLE)
        if item.removable:
            removablecomponents.append(item)
        else:
            unremovablecomponents.append(item)
    return render_to_response(EDIT_TEMPLATE, {"user": request.user, "defaultcomponents": removablecomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents})


def edit_template(request):
    defaultcomponents = TemplateComponent.objects.filter(default=True)
    unremovablecomponents = []
    removablecomponents = []
    customcomponents = TemplateComponent.objects.filter(company=request.user.userprofile.company)
    template = InvoiceTemplate.objects.get(id=request.GET[ID_TEMPLATE])
    for item in defaultcomponents:
        if item.type == IMAGE:
            item.content = item.content.replace("[url]", IMAGES_BASE + "/" + IMAGE_1)
        elif item.type == LOGO:
            item.content = item.content.replace("[url]", IMAGES_BASE + "/" + LOGO_EXAMPLE)
        if item.removable:
            removablecomponents.append(item)
        else:
            unremovablecomponents.append(item)
    return render_to_response(EDIT_TEMPLATE, {"user": request.user, "defaultcomponents": removablecomponents, "unremovablecomponents": unremovablecomponents, "customcomponents": customcomponents, ID_TEMPLATE: template.id, "title_template": template.title, DESC_TEMPLATE: template.description})


def get_template(request):
    template = InvoiceTemplate.objects.get(id=request.GET[ID_TEMPLATE])
    component_instances = TemplateComponentInstance.objects.filter(template=template)
    list = []
    for row in component_instances:
        if row.component.type == IMAGE:
            row.component.content = row.component.content.replace("[url]", IMAGES_BASE + "/" + IMAGE_1)
        elif row.component.type == LOGO:
            row.component.content = row.component.content.replace("[url]", IMAGES_BASE + "/" + LOGO_EXAMPLE)
        list.append({'id': row.id, REFERENCE: row.reference, X: row.position_x, Y: row.position_y, SIZE_X: row.component.size_x, SIZE_Y: row.component.size_y, "component": row.component.id, CONTENT: row.component.content, "removable": row.component.removable, TYPE: row.component.type})
    return HttpResponse(json.dumps(list), content_type="application/json")


def add_custom_component(request):
    saved_component = TemplateComponent(company=request.user.userprofile.company, default=False, removable=True, title=request.POST['title'], size_x=request.POST[SIZE_X], size_y=request.POST[SIZE_Y], content=request.POST[CONTENT])
    saved_component.save()
    return HttpResponse(saved_component.id)


def update_custom_component(request):
    TemplateComponent.objects.filter(pk=request.POST[COMPONENT]).update(title=request.POST['title'], content=request.POST[CONTENT])
    return HttpResponse(request.POST[COMPONENT])


def delete_custom_component(request):
    if request.method == 'GET':
        component = TemplateComponent.objects.get(id=request.GET[COMPONENT])
        instances = TemplateComponentInstance.objects.filter(component=component)
        if instances.exists():
            return HttpResponse("ko")
        else:
            component.delete()
            return HttpResponse("ok", content_type="application/json")
    else:
        return HttpResponse("ko")


def save_template(request):
    if request.POST[ID_TEMPLATE] is "":
        template = InvoiceTemplate(title=request.POST['title_template'], description=request.POST[DESC_TEMPLATE], company=request.user.userprofile.company)
        template.save()
    else:
        template = InvoiceTemplate.objects.get(id=request.POST[ID_TEMPLATE])
        TemplateComponentInstance.objects.filter(template=template).delete()
        InvoiceTemplate.objects.filter(id=request.POST[ID_TEMPLATE]).update(title=request.POST['title_template'], description=request.POST[DESC_TEMPLATE])
    instances = json.loads(request.POST[COMPONENTS])
    for instance in instances:
        TemplateComponentInstance(template=template, reference=instance[REFERENCE],
                                  position_x=instance[X], position_y=instance[Y],
                                  component=TemplateComponent.objects.get(id=instance[COMPONENT])).save()

    return HttpResponse(template.id)


def print_preview(request):
    components = json.loads(request.GET[COMPONENTS])
    output = BytesIO()
    doc = BaseDocTemplate(output, pagesize=size)
    pdf = Pdf(components, size[1], inch, .50)

    def frame(canvas, doc):
        canvas.saveState()
        for item in pdf.header:
            pdf.paint_header_item(item, canvas)
        for item in pdf.footer:
            pdf.paint_footer_item(item, canvas)
        canvas.restoreState()
    doc.addPageTemplates([PageTemplate(frames=Frame(doc.leftMargin, pdf.body_y(), doc.width, pdf.body_y_size()), onPage=frame)])
    story = []
    products = [['Description', 'Category', 'Unit prize', 'Units', 'Tax', 'Amount']]
    for i in range(40):
        products.append(['Product %s' % i, 'Category %s' % i , i, i, i, i])
    story.append(Table(products))
    doc.build(story)
    pdf_output = output.getvalue()
    output.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    response.write(pdf_output)
    return response