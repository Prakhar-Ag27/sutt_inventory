from django import forms

class issue_form(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
