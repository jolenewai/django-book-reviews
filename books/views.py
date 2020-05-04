from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import Book_Form, Author_Form

# Create your views here.
def index(request):
    books = Book.objects.all()

    return render(request, 'books/index.template.html', {
        'books':books,
        'authors': authors
    })

def authors(request):
    authors = Author.objects.all()

    return render(request, 'books/authors.template.html', {
        'authors': authors
    })

def add_book(request):

    if request.method == 'POST':
        add_book_form = Book_Form(request.POST)

        if add_book_form.is_valid():
            add_book_form.save()
        else:
            return render(request, 'books/add_book.template.html', {
                'book_form': book_form
            })
        return redirect(reverse(index))

    else: 

        book_form = Book_Form()
        
        return render(request, 'books/add_book.template.html', {
            'book_form': book_form
        })

def add_author(request):

    if request.method == 'POST':
        add_author_form = Author_Form(request.POST)

        if add_author_form.is_valid():
            add_author_form.save()
        else:
            return render(request, 'books/add_author.template.html', {
                'author_form': author_form
            })
        
        return redirect(reverse(authors)) 
    else:
        author_form = Author_Form()

        return render(request, 'books/add_author.template.html', {
            'author_form': author_form
        })