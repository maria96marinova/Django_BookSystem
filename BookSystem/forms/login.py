from django import forms

class LogInForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['password'].widget.attrs.update({'class': 'form-control col-md-4'})

