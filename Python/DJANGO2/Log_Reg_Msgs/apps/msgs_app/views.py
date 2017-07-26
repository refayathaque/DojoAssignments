from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    context = {
        'session_username' : User.objects.get(id = request.session['user_id']).username,
        'users_minus_self' : User.objects.exclude(id = request.session['user_id'])
    }
    return render(request, 'msgs_app/index.html', context)

def log_out(request):
    del request.session['user_id']
    print '*** IN SESSION? ', 'user_id' in request.session
    return redirect(reverse('log_reg:index'))

def create(request):
    return redirect('msgs:index')
