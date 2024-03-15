from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def home(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/home.html', {'quotes': quotes})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'quotes/author_detail.html', {'author': author})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect("home")
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {form: form})



