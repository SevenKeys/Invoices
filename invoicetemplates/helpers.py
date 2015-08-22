from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
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
BACKGROUND_HEADER = 'background_header'
BACKGROUND_COLUMN_0 = 'background_column_0'
BACKGROUND_COLUMN_1 = 'background_column_1'
BACKGROUND_COLUMN_2 = 'background_column_2'
BACKGROUND_COLUMN_3 = 'background_column_3'
BACKGROUND_COLUMN_4 = 'background_column_4'
BACKGROUND_COLUMN_5 = 'background_column_5'
HORIZONTAL_LINES = 'horizontal_lines'
ALIGNMENT = 'aligment'
VERTICAL_LINES = 'vertical_lines'
BORDER_RIGHT_TABLE = 'border_right_table'
BORDER_BOTTOM_HEADER = 'border_bottom_header'
BORDER_TOP_HEADER = 'border_top_header'


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

    def header_footer(self, canvas):
        canvas.saveState()
        for item in self.header:
            self.paint_header_item(item, canvas)
        for item in self.footer:
            self.paint_footer_item(item, canvas)
        canvas.restoreState()

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


def build_table_style(archetype):
    style = []
    for field in archetype:
        if field.element.code == BACKGROUND_HEADER:
            style.append(('BACKGROUND', (0, 0), (5, 0), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_0:
            style.append(('BACKGROUND', (0, 1), (0, -1), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_1:
            style.append(('BACKGROUND', (1, 1), (1, -1), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_2:
            style.append(('BACKGROUND', (2, 1), (2, -1), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_3:
            style.append(('BACKGROUND', (3, 1), (3, -1), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_4:
            style.append(('BACKGROUND', (4, 1), (4, -1), colors.HexColor(field.value)))
        elif field.element.code == BACKGROUND_COLUMN_5:
            style.append(('BACKGROUND', (5, 1), (5, -1), colors.HexColor(field.value)))
        elif field.element.code == HORIZONTAL_LINES:
            style.append(('LINEBELOW', (0, 1), (-1, -1), 0, colors.HexColor(field.value)))
        elif field.element.code == ALIGNMENT:
            style.append(('ALIGN', (1, 1), (-1, -1), field.value))
        elif field.element.code == VERTICAL_LINES:
            style.append(('LINEBEFORE', (0, 0), (-1, -1), 0.25, colors.HexColor(field.value)))
        elif field.element.code == BORDER_RIGHT_TABLE:
            style.append(('LINEAFTER', (4, 0), (-1, -1), 0.25, colors.HexColor(field.value)))
        elif field.element.code == BORDER_BOTTOM_HEADER:
            style.append(('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor(field.value)))
        elif field.element.code == BORDER_TOP_HEADER:
            style.append(('LINEABOVE', (0, 0), (-1, 0), 2, colors.HexColor(field.value)))
    return style