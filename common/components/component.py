from django.views.generic import TemplateView

class ViewComponent(TemplateView):
    def __init__(self, template_name):
        self.data = {}
        self.template_name = template_name
        super(TemplateView, self).__init__()

    def render_data(self):
        pass  # override this function to get preloaded data to template

