from django import forms

from .models import Pdf

class PdfForm(forms.ModelForm):

    class Meta:
        model = Pdf
        fields = ('report_name', 'data', 'file_format', 'template_name', 'service_url',)