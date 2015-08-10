from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
from .models import *
from .forms import InvoiceForm
from django.http import HttpResponse
import json
from io import BytesIO
from reportlab.platypus import Paragraph, Frame, BaseDocTemplate, PageTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus.flowables import Image
import logging
import os
from os.path import join
import re

logger = logging.getLogger("main.views.templates")
size = A4
styles = getSampleStyleSheet()
TYPE_COMPONENT = 'type'
LOGO = "logo"
IMAGE = "image_1"
PRINCIPAL = "principal"
IMAGES_BASE = "static/images"
IMAGE_1 = "invoice.jpg"
LOGO_EXAMPLE = "kairos_logo.jpg"


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
        if item.type == IMAGE:
            item.content = item.content.replace("[url]", "/" + IMAGES_BASE + "/" + IMAGE_1)
        elif item.type == LOGO:
            item.content = item.content.replace("[url]", "/" + IMAGES_BASE + "/" + LOGO_EXAMPLE)
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
        if item.type == IMAGE:
            item.content = item.content.replace("[url]", IMAGES_BASE + "/" + IMAGE_1)
        elif item.type == LOGO:
            item.content = item.content.replace("[url]", IMAGES_BASE + "/" + LOGO_EXAMPLE)
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
        if row.component.type == IMAGE:
            row.component.content = row.component.content.replace("[url]", IMAGES_BASE + "/" + IMAGE_1)
        elif row.component.type == LOGO:
            row.component.content = row.component.content.replace("[url]", IMAGES_BASE + "/" + LOGO_EXAMPLE)
        list.append({'id': row.id, 'reference': row.reference, 'position_x': row.position_x, 'position_y': row.position_y, "size_x": row.component.size_x, "size_y": row.component.size_y, "component": row.component.id, "content": row.component.content, "removable": row.component.removable, "type": row.component.type})
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
    output = BytesIO()
    doc = BaseDocTemplate(output, pagesize=size)
    pdf = Pdf(components, size[1], inch, .50)

    def page_frame(canvas, doc):
        canvas.saveState()
        for item in pdf.header:
            pdf.paint_header_component(item, canvas)
        for item in pdf.footer:
            pdf.paint_footer_component(item, canvas)
        canvas.restoreState()
    doc.addPageTemplates([PageTemplate(id="test", frames=Frame(doc.leftMargin, pdf.content_y_position(), doc.width, pdf.content_y_size()), onPage=page_frame)])
    story = []
    products = [['Description', 'Category', 'Unit prize', 'Units', 'Tax', 'Amount']]
    for i in range(40):
        products.append(['Product %s' % i, 'Category %s' % i, i, i, i, i])
    story.append(Table(products))
    doc.build(story)
    pdf_output = output.getvalue()
    output.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    response.write(pdf_output)
    return response


class Pdf(object):
    def __init__(self, elements, size_y_base, unit, margin):
        self.center_element = 0
        self.last_header_y_position = 0
        self.last_size_y_header = 0
        self.first_footer_y_position = 100000
        self.last_footer_y_position = 0
        self.last_footer_y_size = 0
        self.header = []
        self.footer = []
        self.elements = elements
        self.space_footer_y = 0
        self.space_header_y = 0
        self.size_y_base = size_y_base
        self.unit = unit
        self.margin = margin
        for entity in elements:
            if entity['type'] == PRINCIPAL:
                self.center_element = entity['position_y']
        for element in elements:
            if element['position_y'] > self.center_element:
                self.footer.append(element)
                if element['position_y'] < self.first_footer_y_position:
                    self.first_footer_y_position = element['position_y']
                if element['position_y'] > self.last_footer_y_position:
                    self.last_footer_y_position = element['position_y']
                    self.last_footer_y_size = element['size_y']
            elif element['position_y'] < self.center_element:
                self.header.append(element)
                if element['position_y'] > self.last_header_y_position:
                    self.last_header_y_position = element['position_y']
                    self.last_size_y_header = element['size_y']
        self.space_footer_y = self.last_footer_y_position + self.last_footer_y_size - self.first_footer_y_position
        self.space_header_y = self.last_header_y_position + self.last_size_y_header - 1

    def x_position(self, element):
        return element['position_x']*self.unit

    def x_size(self, element):
        return element['size_x']*self.unit

    def y_size(self, element):
        return element['size_y']*self.unit

    def header_y_position(self, element):
        return self.size_y_base - (element['position_y'] + element['size_y'] - 1)*self.unit

    def footer_y_position(self, element):
        return self.size_y_base - self.content_y_size()

    def content_y_position(self):
        return self.size_y_base - self.space_header_y*self.unit - self.content_y_size()

    def content_y_size(self):
        return self.size_y_base - (self.space_header_y + self.space_footer_y)*self.unit

    def paint_header_component(self, component, canvas):
        if component[TYPE_COMPONENT] == IMAGE or component[TYPE_COMPONENT] == LOGO:
            image = component['content'].split("/")
            canvas.drawImage(join(os.getcwd(), IMAGES_BASE, image[5].split('">')[0]), self.x_position(component), self.header_y_position(component), self.x_size(component), self.y_size(component))
        else:
            Frame(self.x_position(component), self.header_y_position(component), self.x_size(component), self.y_size(component)).addFromList(self.get_widgets(component['content']), canvas)

    def paint_footer_component(self, component, canvas):
        if component[TYPE_COMPONENT] == IMAGE or component[TYPE_COMPONENT] == LOGO:
            image = component['content'].split("/")
            canvas.drawImage(join(os.getcwd(), "static/images", image[5].split('">')[0]), self.x_position(component), self.footer_y_position(component), self.x_size(component), self.y_size(component))
        else:
            Frame(self.x_position(component), self.footer_y_position(component), self.x_size(component), self.y_size(component)).addFromList(self.get_widgets(component['content']), canvas)

    def get_widgets(self, convert_to_paragraph):
        convert_to_paragraph = self.translate_string(convert_to_paragraph)
        paragraphs = []
        regex = re.compile('<h1>' + '(.*?)' + '</h1>')
        result = regex.search(convert_to_paragraph)
        if result:
            paragraphs.append(Paragraph(self.translate_string(result.groups(1)[0]), styles['Heading1']))
        regex = re.compile('<h2>' + '(.*?)' + '</h2>')
        result = regex.search(convert_to_paragraph)
        if result:
            paragraphs.append(Paragraph(self.translate_string(result.groups(1)[0]), styles['Heading2']))
        regex = re.compile('<p>' + '(.*?)' + '</p>')
        result = regex.search(convert_to_paragraph)
        if result:
            paragraphs.append(Paragraph(self.translate_string(result.groups(0)[0]), styles['Normal']))
        regex = re.compile('<address>' + '(.*?)' + '</address>')
        result = regex.search(convert_to_paragraph)
        if result:
            paragraphs.append(Paragraph(self.translate_string(result.groups(0)[0]), styles['Normal']))
        return paragraphs

    def get_widget(self, to_paragraph, start_string, end_string, style):
        paragraphs = []
        regex = re.compile(start_string + '(.*?)' + end_string)
        result = regex.search(to_paragraph)
        if result:
            paragraphs.append(Paragraph(self.translate_string(result.groups(0)[0]), styles[style]))

        return paragraphs

    def translate_string(self, string_to_translate):
        return string_to_translate.replace("<br>", "<br/>").replace("<strong>", "<b>").replace("</strong>", "</b>")


class AddInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create_invoice.html'
    success_url = '/invoices/success.html'