from django import forms
from .models import Book, Author


class Book_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'ISBN', 'desc')


class Author_Form(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')

