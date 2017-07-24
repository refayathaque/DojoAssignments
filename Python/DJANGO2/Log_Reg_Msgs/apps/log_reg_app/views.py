from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'log_reg_app/index.html')

def registration(request):
    validation_tuple = User.objects.registration_validation(request.POST)
    if validation_tuple[0] == True:
        request.session['user_id'] = User.objects.get(email=validation_tuple[1]).id
    else:
        for error in validation_tuple[1]:
            messages.error(request, error)
    return redirect('/')
