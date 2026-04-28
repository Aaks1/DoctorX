from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    """Form for booking appointments"""
    class Meta:
        model = Appointment
        fields = ['symptoms']
        widgets = {
            'symptoms': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'rows': 4,
                'placeholder': 'Please describe your symptoms or reason for this appointment...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].label = 'Reason for Visit <span class="text-red-500">*</span>'
        self.fields['symptoms'].required = True

class BookAppointmentForm(forms.ModelForm):
    """Form for booking appointments with time selection"""
    class Meta:
        model = Appointment
        fields = ['symptoms']
        widgets = {
            'symptoms': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'rows': 4,
                'placeholder': 'Please describe your symptoms or reason for this appointment...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].label = 'Reason for Visit <span class="text-red-500">*</span>'
        self.fields['symptoms'].required = True
