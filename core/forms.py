from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'purpose', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'სახელი და გვარი'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+995 5XX XX XX XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email (არასავალდებულო)'}),
            'purpose': forms.Select(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'შეტყობინება (არასავალდებულო)'}),
        }
        labels = {
            'name': 'სახელი, გვარი',
            'phone': 'ტელეფონი',
            'email': 'Email',
            'purpose': 'სერვისი',
            'message': 'შეტყობინება',
        }
