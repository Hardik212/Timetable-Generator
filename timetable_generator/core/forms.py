from django import forms
from core.models import Program

class programforms(forms.ModelForm):
    class Meta:
        model=Program
        fields=['id']