from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Author, Quote, Tag
from .forms import AuthorForm, QuoteForm
from django.core.paginator import Paginator
from django.db.models import Count

def home(request, page=1):
    quotes = Quote.objects.all().order_by("-created_at")

    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    top_tags = Tag.objects.annotate(tag_count=Count("quote")).order_by("-tag_count")[
        :10
    ]

    return render(
        request,
        "quotes/home.html",
        context={
            "top_tags": top_tags,
            "quotes": quotes_on_page,
        },
    )

def author(request, author_name):
    author = Author.objects.get(name=author_name)
    if not author:
        author = None

    return render(request, "quotes/author_detail.html", context={"author": author})

def tag(request, tag_name):
    quotes = Quote.objects.filter(tags__name=tag_name).order_by("-created_at")
    top_tags = Tag.objects.annotate(tag_count=Count("quote")).order_by("-tag_count")[
        :10
    ]
    return render(
        request,
        "quotes/tag_view.html",
        context={
            "top_tags": top_tags,
            "tag_name": tag_name,
            "quotes": quotes,
        },
    )


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuoteForm()

    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
        
    return render(request, 'quotes/add_author.html', {'form': form})



