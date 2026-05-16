from django import forms
from django.core.validators import RegexValidator
from .models import Lead


class LeadForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9\s\-]{9,20}$',
                message="ტელეფონის ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს და '+' ნიშანს. / Phone number must contain only digits and '+' sign."
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '+995 5XX XX XX XX',
            'pattern': r'^\+?[0-9\s\-]{9,20}$',
            'title': 'შეიყვანეთ ვალიდური ტელეფონის ნომერი (+ ნიშანი და ციფრები)'
        }),
        label='ტელეფონი / Phone'
    )

    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'purpose', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'სახელი და გვარი / Name & Surname'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            }),
            'purpose': forms.Select(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'შეტყობინება / Message (optional)'
            }),
        }
        labels = {
            'name': 'სახელი, გვარი / Name',
            'email': 'Email',
            'purpose': 'სერვისი / Service',
            'message': 'შეტყობინება / Message',
        }
