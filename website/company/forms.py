from django import forms
from company.models import Contact_model


class Contact_form(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # sensor = forms.CharField()
    # text = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Contact_model
        fields = "__all__"
