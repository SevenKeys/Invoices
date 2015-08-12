from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import logging
import os
from os.path import join
import re


logger = logging.getLogger("main.helpers.templates")
size = A4
styles = getSampleStyleSheet()
TYPE_COMPONENT = 'type'
LOGO = "logo"
IMAGE = "image_1"
IMAGE_1 = "invoice.jpg"
PRINCIPAL = "principal"
IMAGES_BASE = "static/images"
LOGO_EXAMPLE = "kairos_logo.jpg"
CUSTOM = 'custom'
TYPE = 'type'
CONTENT = 'content'
X = 'position_x'
Y = 'position_y'
SIZE_X = 'size_x'
SIZE_Y = 'size_y'
REFERENCE = 'reference'
COMPONENT = 'id_component'


class Pdf(object):
    def __init__(self, elements, size_y_base, unit, margin):
        self.center_element = 0
        self.last_header_y = 0
        self.first_footer_y = 100000
        self.last_footer_y = 0
        self.header = []
        self.footer = []
        self.size_y_base = size_y_base
        self.unit = unit
        self.margin = margin
        self.last_footer_y_size = 0
        self.last_size_y_header = 0
        for entity in elements:
            if entity[TYPE] == PRINCIPAL:
                self.center_element = entity[Y]
        for item in elements:
            if item[Y] > self.center_element:
                self.footer.append(item)
                if item[Y] < self.first_footer_y:
                    self.first_footer_y = item[Y]
                if item[Y] > self.last_footer_y:
                    self.last_footer_y = item[Y]
                    self.last_footer_y_size = item[SIZE_Y]
            elif item[Y] < self.center_element:
                self.header.append(item)
                if item[Y] > self.last_header_y:
                    self.last_header_y = item[Y]
                    self.last_size_y_header = item[SIZE_Y]
        self.space_footer_y = self.last_footer_y + self.last_footer_y_size - self.first_footer_y
        self.space_header_y = self.last_header_y + self.last_size_y_header - 1

    def x(self, item):
        return item[X]*self.unit

    def x_size(self, item):
        return item[SIZE_X]*self.unit

    def y_size(self, item):
        return item[SIZE_Y]*self.unit

    def header_y(self, item):
        return self.size_y_base - (item[Y] + item[SIZE_Y] - 1)*self.unit

    def footer_y(self, item):
        return self.body_y() - (item[Y] - self.first_footer_y + item[SIZE_Y])*self.unit

    def body_y(self):
        return self.size_y_base - self.space_header_y*self.unit - self.body_y_size()

    def body_y_size(self):
        return self.size_y_base - (self.space_header_y + self.space_footer_y)*self.unit

    def paint_header_item(self, item, canvas):
        if item[TYPE] == IMAGE or item[TYPE] == LOGO:
            image = item[CONTENT].split("/")
            canvas.drawImage(join(os.getcwd(), IMAGES_BASE, image[5].split('">')[0]), self.x(item), self.header_y(item), self.x_size(item), self.y_size(item))
        else:
            parser = StringTranslator(item[CONTENT])
            Frame(self.x(item), self.header_y(item), self.x_size(item), self.y_size(item)).addFromList(parser.widgets(), canvas)

    def paint_footer_item(self, item, canvas):
        if item[TYPE] == IMAGE or item[TYPE] == LOGO:
            image = item[CONTENT].split("/")
            canvas.drawImage(join(os.getcwd(), IMAGES_BASE, image[5].split('">')[0]), self.x(item), self.footer_y(item), self.x_size(item), self.y_size(item))
        else:
            parser = StringTranslator(item[CONTENT])
            Frame(self.x(item), self.footer_y(item), self.x_size(item), self.y_size(item)).addFromList(parser.widgets(), canvas)


class StringTranslator:
    def __init__(self, string_to_translate):
        self.content = string_to_translate.replace("<br>", "<br/>").replace("<strong>", "<b>").replace("</strong>", "</b>")

    def widgets(self):
        paragraphs = []
        paragraphs = paragraphs + self.widget(self.content, '<h1>', '</h1>', 'Heading1')
        paragraphs = paragraphs + self.widget(self.content, '<h2>', '</h2>', 'Heading2')
        paragraphs = paragraphs + self.widget(self.content, '<p>', '</p>', 'Normal')
        paragraphs = paragraphs + self.widget(self.content, '<address>', '</address>', 'Normal')
        return paragraphs

    def widget(self, to_paragraph, start_tag, end_tag, style):
        paragraphs = []
        regex = re.compile(start_tag + '(.*?)' + end_tag)
        result = regex.search(to_paragraph)
        if result:
            paragraphs.append(Paragraph(result.groups(0)[0], styles[style]))
        return paragraphs
