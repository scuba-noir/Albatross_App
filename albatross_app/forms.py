import django
import django.forms as forms
from django.forms import ModelForm
from albatross_app.models import contactFormRecords
from django.core.validators import MinValueValidator, MaxValueValidator

class contactForm(ModelForm):

    class Meta:
        model = contactFormRecords
        fields = ['first_name', 'last_name', 'email','message']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':"form-control form-control-sm"}),
            'last_name':forms.TextInput(attrs={'class':"form-control form-control-sm"}),
            'email':forms.EmailInput(attrs={'class':"form-control form-control-sm"}),
            'message':forms.Textarea(attrs={'class':"form-control form-control-sm"})
        }

    