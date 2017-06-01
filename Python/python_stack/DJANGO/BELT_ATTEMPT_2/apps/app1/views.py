from django.shortcuts import render, redirect

from .models import User

from django.contrib import messages

def index(request):
    print "*"*10
    return render(request, 'app1/index.html')

def registration(request):

    results = User.objects.registration(request.POST)

    if results[0]:
        request.session['email'] = results[1]

        return redirect('/app2/quotes')

    else:

        for err in results[1]:
            messages.error(request, err)

        return redirect('/')

def login(request):

    results = User.objects.login(request.POST)

    if results[0]: # results[0] is a tuple
        request.session['email'] = results[1]

        return redirect('/app2/quotes')

    else:

        for err in results[1]: # (False, errors)
            messages.error(request, err)

        return redirect('/')

def quotes(request):
    return redirect('/app2/quotes')
