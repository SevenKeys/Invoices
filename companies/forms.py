from django import forms
from .models import Company
from users.models import UserProfile


class CompanyForm(forms.ModelForm):
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    street = forms.CharField()
    city = forms.CharField()
    postcode = forms.IntegerField()
    country = forms.CharField()
    website = forms.CharField()
    full_user_name = forms.CharField()
    name = forms.CharField(label='Company name')

    class Meta:
        model = Company
        fields = ['full_user_name', 'name', 'phone_number', 'email', 'street',
                  'city', 'postcode', 'country', 'website', 'reg_code']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        try:
            contact = user.userprofile.contact
            super(CompanyForm, self).__init__(*args, **kwargs)
            self.fields['phone_number'] = forms.IntegerField(initial=contact.phone_number if contact else '',
                                                             label='Phone number')
            self.fields['email'] = forms.EmailField(initial=contact.email if contact else '',
                                                    label='Email')
            self.fields['city'] = forms.CharField(initial=contact.city if contact else '',
                                                  label='City')
            self.fields['street'] = forms.CharField(initial=contact.street if contact else '',
                                                    label='Street')
            self.fields['postcode'] = forms.IntegerField(initial=contact.postcode if contact else '',
                                                         label='Postcode')
            self.fields['country'] = forms.CharField(initial=contact.country if contact else '',
                                                     label='Country')
            self.fields['website'] = forms.CharField(initial=contact.website if contact else '',
                                                     label='Website')
        except UserProfile.DoesNotExist:
            super(CompanyForm, self).__init__(*args, **kwargs)
