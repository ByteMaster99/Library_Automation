from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields =['book_name','author','price','status','created_by']

