from django.shortcuts import render

from .models import Books

def index(request):
    # Books.objects.create(title= 'British Bake-Off', author= 'Claudia Fossatti', category= 'Dumb Books')
    # Books.objects.create(title= 'Australian Bake-Off', author= 'Horacio Fossatti', category= 'Dumb Books')
    # Books.objects.create(title= 'Belgian Bake-Off', author= 'Eugene Fossatti', category= 'Dumb Books')
    # Books.objects.create(title= 'French Bake-Off', author= 'Arif Fossatti', category= 'Dumb Books')
    # Books.objects.create(title= 'Indian Bake-Off', author= 'Ausar Fossatti', category= 'Dumb Books')
    books = Books.objects.all()
    print books
    for i in books: # i is variable used to iterate through table 'Books'
        print i.title, i.author, i.published_date, i.category, i.in_print
    return render(request, 'books_app/index.html')
