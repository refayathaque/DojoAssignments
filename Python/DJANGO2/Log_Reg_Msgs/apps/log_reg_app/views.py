from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'log_reg_app/index.html')

def registration(request):
    user_created = User.objects.registration_validation(request.POST)
    print user_created
    return redirect(request, '/')
