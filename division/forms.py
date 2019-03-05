from django import forms
from . import models

class ContactUsForms(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ['nama', 'email', 'no_telepon', 'subyek', 'pesan']
