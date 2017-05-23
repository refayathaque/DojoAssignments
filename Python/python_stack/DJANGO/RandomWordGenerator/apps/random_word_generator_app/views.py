from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'random_word_generator_app/index.html')

def random_word_generator(request):
    random_letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'y', 'q', 'w', 'e', 'o', 'p']
    string = ""

    for i in range(0, 14):
        random_letter = random.choice(random_letters)
        string += random_letter # appending to string

    if request.method == "POST": # SETTING SESSIONS!
		request.session['random_word'] = string
		request.session['count'] += 1
		return redirect('/') # bc POST
    else:
        return redirect('/')
