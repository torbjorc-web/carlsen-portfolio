from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'selected_service', 'project_type', 'message']
        labels = {
            'project_type': 'Service or project type',
            'message': 'Tell me about your project',
        }
        widgets = {
            'selected_service': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'project_type': forms.TextInput(attrs={'placeholder': 'What service are you interested in?'}),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Tell me about your project, goals, timeline, or what you want help with.'}),
        }
