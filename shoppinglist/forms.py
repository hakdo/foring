from django import forms
from . models import SimpleList
import json

class SimpleListForm(forms.ModelForm):
    class Meta:
        model = SimpleList
        fields = ('shortname', 'contents','sharedwith')
        labels = {
                'shortname': (u'Listenavn'),
                'contents': (u'Innhold'),
                'sharedwith': (u'Delt med'),
        }
        help_texts = {
            'contents': (u'Linjeskift mellom hvert element i lista.'),
        }

class loginForm(forms.Form):
    username=forms.CharField(max_length=200,label='Brukernavn')
    password=forms.CharField(max_length=30,label='Passord',widget=forms.PasswordInput())

class registernewForm(forms.Form):
    username=forms.CharField(max_length=20,label='Ønsket brukernavn')
    email=forms.EmailField(label='E-post')
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(),label='Passord')
