from django import forms
from company.models import Contact_model
from django.utils.translation import ugettext_lazy as _


class Contact_form(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # sensor = forms.CharField()
    # text = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = Contact_model
        fields = "__all__"
        labels = {
            'name': _('Your Name (required)'),
            'email': _('Your Email (required)'),
            'sensor': _('Which sensor are you interested in?'),
            'message': _('Your Message'),
        }
