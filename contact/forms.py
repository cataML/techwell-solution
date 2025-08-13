from django import forms
from .models import Contact

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Enter your full name',
            'email': 'Enter your email',
            'subject': 'Enter the subject',
            'message': 'Type your message here'
         }
            
        for field_name, field in self.fields.items():
            field.required = True  # Django validation
            field.widget.attrs.update({
                'placeholder': placeholders.get(field_name, ''),
                'required': 'required'  # HTML5 browser validation
        })