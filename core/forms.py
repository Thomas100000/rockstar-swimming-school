from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'mobile_number']
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'minlength': '2', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'required': True, 'placeholder': 'Email Address'}),
            'mobile_number': forms.TextInput(attrs={
                'required': True, 
                'pattern': r'^\+?1?\d{9,15}$', 
                'title': 'Enter a valid 10-15 digit mobile number, e.g., +1234567890',
                'placeholder': 'Mobile Number'
            }),
        }
