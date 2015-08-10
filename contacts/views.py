# Create your views here.
# mixin to get contact and data
class ContactMixin(object):
    def get_contact(self, **kwargs):
        user = self.request.user
        contact = user.userprofile.contact
        return contact
