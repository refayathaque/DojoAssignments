from django.shortcuts import render, HttpResponse, redirect

from .models import User

from django.contrib import messages

# INDEX (Displays login and registration forms)
def index(request):

    return render(request, 'app1/index.html')
####

# LOGIN (Routes login validation from UserManager in Models)
def login(request):

    results = User.objects.login(request.POST)

    if results[0]: # results[0] is a tuple

        request.session['logged_in_user_username'] = results[1]
        request.session['registered_user_username'] = None
        print 'in session: ' + request.session['logged_in_user_username'] # refayathaque

        return redirect('app2/travels')

    else:

        for err in results[1]: # (False, errors)
            messages.error(request, err)

        return redirect('/')
####

# REGISTRATION (Routes registration validation from UserManager in Models)
def registration(request):

    results = User.objects.registration(request.POST)

    if results[0]:

        request.session['registered_user_username'] = results[1]
        request.session['logged_in_user_username'] = None
        print 'in session: ' + request.session['registered_user_username']

        return redirect('app2/travels')

    else:

        for err in results[1]:
            messages.error(request, err)

        return redirect('/')
####

# Hack to get app2 /travels route to work
def travels(request):

    return redirect('app2/travels')
####
