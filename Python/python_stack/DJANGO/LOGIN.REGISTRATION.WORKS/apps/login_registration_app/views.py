from django.shortcuts import render, HttpResponse, redirect

from .models import User

from django.contrib import messages

def index(request):
    print "*"*50
    return render(request, 'login_registration_app/index.html')

def login(request):
      results = User.objects.login(request.POST) #request.POST passes in dict
      context = {
            'logged_in_user' : results,
            'registered_users' : User.objects.all()
      }
      print results
      if results[0]: # results[0] is a tuple
        #   return redirect('/success')
          return render(request, 'login_registration_app/success.html', context)
      else:
          for err in results[1]: # (False, errors)
              messages.error(request, err)
          return redirect('/')


def registration(request):
    results = User.objects.registration(request.POST)
    if results[0]:
        return redirect('/success')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/')

def success(request):
    return render(request, 'login_registration_app/success.html')

def reset(request):
    return redirect('/')
