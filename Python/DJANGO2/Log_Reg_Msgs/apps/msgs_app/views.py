from django.shortcuts import render, redirect
from .models import User, Message
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    context = {
        'session_user' : User.objects.get(id = request.session['user_id']),
        # REVERSE LOOK UP implemented here with 'received' and 'sent' messages
        # 'session_username' : User.objects.get(id = request.session['user_id']).username,
        'users_minus_self' : User.objects.exclude(id = request.session['user_id'])
    }
    return render(request, 'msgs_app/index.html', context)

def log_out(request):
    del request.session['user_id']
    print '*** IN SESSION? ', 'user_id' in request.session
    return redirect(reverse('log_reg:index'))

def create(request):
    validation_tuple = Message.messageManager.send(request.POST['message'], request.session['user_id'], request.POST['users_minus_self'])
    print validation_tuple
    if validation_tuple[0] == False:
        for error in validation_tuple[1]:
            messages.error(request, error)
    return redirect('msgs:index')
