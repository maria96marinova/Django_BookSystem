from django import forms

class PublisherForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    country = forms.CharField(label='city', max_length=50)

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['country'].widget.attrs.update({'class': 'form-control col-md-4'})