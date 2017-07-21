from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    return render(request, 'session_words/index.html')

def add_words(request):
    if 'word' in request.session:
        context = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'font_size': request.POST['font_size'],
            'datetime': datetime.now().strftime('%-I:%M %p, %b %-d, %Y')
        }
        request.session['word'].append(context)
    else:
        request.session['word'] = []
        context = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'font_size': request.POST['font_size'],
            'datetime': datetime.now().strftime('%-I:%M %p, %b %-d, %Y')
        }
        request.session['word'].append(context)
    request.session.modified = True
    return redirect('/')

def clear(request):
    del request.session['word']
    return redirect('/')
