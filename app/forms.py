from django import forms

class Form(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    