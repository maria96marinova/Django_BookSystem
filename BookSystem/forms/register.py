from django import forms

class RegisterForm(forms.Form):

    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    country = forms.CharField(label='Country', max_length=50)
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['country'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['username'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['password'].widget.attrs.update({'class': 'form-control col-md-4'})
