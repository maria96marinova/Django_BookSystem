from django import forms

from BookSystem.services import CategoryService, PublisherService, AuthorService


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    description = forms.CharField(label='Description', max_length=50)
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ChoiceField(label='Category', choices=CategoryService.getAll().values_list("id", "name"))
    publisher = forms.ChoiceField(label='Publisher', choices=PublisherService.getAll().values_list("id", "name"))
    authors = forms.MultipleChoiceField(choices=AuthorService.getAll().values_list("id", "first_name"))

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control col-md-4'})
        self.fields['description'].widget.attrs.update({'class': 'form-control col-md-4'})


