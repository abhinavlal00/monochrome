from django import forms
from myapp.models import Contact

class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = {'name','email','number','message'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-group'}),
            'email':forms.TextInput(attrs={'class':'form-control form-group'}),
            'number':forms.TextInput(attrs={'class':'form-control form-group'}),
            'message':forms.TextInput(attrs={'class':'form-control form-group'}),
        }
