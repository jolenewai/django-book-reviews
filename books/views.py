from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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


def update_book(request, book_id):
    # 1. retrieve the book which we are editing
    book_being_updated = get_object_or_404(Book, pk=book_id)

    # 2. if the update form is submitted
    if request.method == 'POST':

        # 3. create the form and fill in the user's data. Also specify
        # this is to update an existing model (the instance argument)
        book_form = Book_Form(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/update.template.html', {
                'form': book_form
            })
    else:
        # 4. create the form and fill it with data from book instance
        # book_form = Book_Form(instance=book_being_updated)
        book_form = Book_Form(instance=book_being_updated)

        return render(request, 'books/update.template.html', {
            'form': book_form
        })


def update_author(request, author_id):
    author_being_updated = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':

        author_form = Author_Form(request.POST, instance=author_being_updated)

        if author_form.is_valid():
            author_form.save()
            return redirect(reverse(authors))
        else:
            return render(request, 'books/update.template.html', {
                'form': author_form
            })
    else:
        author_form = Author_Form(instance=author_being_updated)

        return render(request, 'books/update.template.html', {
            'form': author_form
        })


def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book_to_delete.delete()
        return redirect(reverse(index))
    else:
        return render(request, 'books/delete.template.html', {
            'book': book_to_delete
        })


def delete_author(request, author_id):
    author_to_delete = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author_to_delete.delete()
        return redirect(reverse(authors))
    else: 
        return render(request, 'books/delete_author.template.html', {
            'author': author_to_delete
        })