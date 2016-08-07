from django import forms
from . models import SimpleList

class SimpleListForm(forms.ModelForm):
    class Meta:
        model = SimpleList
        fields = ('shortname', 'contents')
        labels = {
                'shortname': (u'Name'),
                'contents': (u'List'),
        }

class loginForm(forms.Form):
    username=forms.CharField(max_length=200,label='Brukernavn')
    password=forms.CharField(max_length=30,label='Passord',widget=forms.PasswordInput())

class registernewForm(forms.Form):
    username=forms.CharField(max_length=20,label='Ønsket brukernavn')
    email=forms.EmailField(label='E-post')
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(),label='Passord')
