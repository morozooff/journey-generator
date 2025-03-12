from django import forms
from .models import Request

class TravelForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['region', 'purpose', 'duration']