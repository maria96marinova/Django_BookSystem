from django import forms

class AuthorForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    type = forms.CharField(label='Type', max_length=50)

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['type'].widget.attrs.update({'class': 'form-control col-md-4'})

