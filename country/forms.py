from django import forms


class CountryForm(forms.Form):
    tags = forms.CharField(label='tags', max_length=100)