from django import forms
from core.models import Course

class courseforms(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"