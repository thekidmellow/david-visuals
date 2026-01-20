from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address_line1', 'address_line2', 'city', 'country', 'postal_code']
        
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'address_line1': forms.TextInput(attrs={'placeholder': 'Address line 1'}),
            'address_line2': forms.TextInput(attrs={'placeholder': 'Address line 2'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal code'}),
        }