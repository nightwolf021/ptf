from django import forms


class message_form(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    subject = forms.CharField(max_length=128)
    message = forms.CharField(max_length=2048)