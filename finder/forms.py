from django import forms
from .models import Property

class propertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'price', 'size_length', 'size_width', 'size_total']