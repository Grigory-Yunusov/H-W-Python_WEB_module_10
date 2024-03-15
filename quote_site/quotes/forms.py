from django.forms import ModelForm, CharField,TextInput, DateField, DateInput, ModelChoiceField, Select
from .models import Author, Quote

class AuthorForm(ModelForm):
    name = CharField(max_length=40, min_length=2, widget=TextInput(attrs={"class": "form-control"}))
    birth_date = DateField(widget=DateInput(attrs={"class": "form-control"})) 
    bio = CharField(max_length=4000, min_length=30, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'bio']


class QuoteForm(ModelForm):
    text = CharField(max_length=1000, min_length=40, widget=TextInput(attrs={"class": "form-control"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('name'), widget=Select(attrs={"class": "form-select"}))

    class Meta:
        model = Quote
        fields = ['text', 'author', ]