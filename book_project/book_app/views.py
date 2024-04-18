from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm


# Create your views here.

def book_list(request):
    books = Book.objects.all()# Retrieve all books from the database
    return render (request,"book_list.html",{'books':books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to the main page after successful form submission
    else:
        form = BookForm()
        return render(request,'book_form.html',{'form':form})