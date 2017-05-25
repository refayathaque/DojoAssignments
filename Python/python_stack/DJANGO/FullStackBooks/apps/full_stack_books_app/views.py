from django.shortcuts import render, HttpResponse, redirect

from .models import Book

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'full_stack_books_app/index.html', context)

def book_input(request):

    Book.objects.create(title = request.POST['title'], author = request.POST['author'], category = request.POST['category'])

    books = Book.objects.all()

    print books

    for i in books:
        print i.title, i.author, i.category

    return redirect('/')
