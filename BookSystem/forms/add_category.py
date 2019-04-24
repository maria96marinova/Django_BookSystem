from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)