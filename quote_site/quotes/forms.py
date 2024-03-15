from django.forms import ModelForm, CharField,TextInput, DateField
from .models import Author, Quote

class AuthorForm(ModelForm):
    # name = CharField(max_length=40, min_length=2, widget=TextInput())
    # birth_date = DateField() #???????
    # bio = CharField(max_length=4000, min_length=30, widget=TextInput())

    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'bio']


class QuoteForm(ModelForm):
    # text = CharField(max_length=1000, min_length=40, widget=TextInput())
    # author =CharField(max_length=40, min_length=2, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['text', 'author', ]