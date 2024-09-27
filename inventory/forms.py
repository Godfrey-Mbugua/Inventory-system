from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
