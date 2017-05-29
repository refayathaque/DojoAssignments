from django.shortcuts import render, HttpResponse, redirect

from .models import User

from django.contrib import messages

def index(request):
    return render(request, 'login_registration_app/index.html')

def login(request):
    results = User.objects.login(request.POST)
    if results[0]: # results[0] is a tuple
        request.session['logged_in_user_email'] = results[1]
        request.session['registered_user_email'] = None
        print 'in session: ' + request.session['logged_in_user_email'] # refayathaque@gmail.com
        return redirect('teams_app/success')
    else:
        for err in results[1]: # (False, errors)
            messages.error(request, err)
        return redirect('/')

def registration(request):
    results = User.objects.registration(request.POST)
    if results[0]:
        request.session['registered_user_email'] = results[1]
        request.session['logged_in_user_email'] = None
        print 'in session: ' + request.session['registered_user_email']
        return redirect('teams_app/success')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/')

def success(request): # Claudia hack to get teams_app /success route to work
    return redirect('teams_app/success')
