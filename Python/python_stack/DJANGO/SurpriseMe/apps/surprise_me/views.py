from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print "*"*50
    return render(request, 'surprise_me/index.html')

def number_input(request):
    print "*"*50
    if request.method == "POST": # SETTING SESSIONS!
        request.session['number'] = request.POST['number']
        return redirect('/results') # bc POST

    else:
        return redirect('/')

def results(request):
    list = ['Apple Macbook', 'Apple Macbook Pro', 'Apple Macbook Air', 'Samsung Galaxy S8', 'OnePlus 3T', 'Salmon Sandwich']
    random_items = random.sample(list, int(request.session['number']))

    context = {
        'key_for_random_stuff' : ', '.join(random_items),
        'number' : request.session['number'] # can also just have 'request.session.name' in html template... :|
    }

    return render(request, 'surprise_me/results.html', context) # Django can take in only ONE dictionary as argument
                                                                # so put all information in it, traversing through is
                                                                # done with dot notation and accessing keys...
