from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count'] = 1
    context = {
        'random' : get_random_string(length=14)
    }
    return render(request, "random_word_generator/index.html", context)

def reset(request):
    del request.session['count']
    return redirect('/')
