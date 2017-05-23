from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

def index(request):
    print "*"*50
    if 'log' in request.session:
        pass
    else:
        request.session['log'] = []
    if 'current_gold' in request.session:
        pass
    else:
        request.session['current_gold'] = 0
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.method == "POST": # SETTING SESSIONS!
        if(request.POST['building'] == 'farm'):
            q = random.randrange(10, 21)
            request.session['current_gold'] += q
            print q
            request.session['log'].insert(0,('You have earned {} gold from the farm @ {}'.format(q, datetime.now())))
            return redirect('/')
        elif(request.POST['building'] == 'cave'):
            q = random.randrange(5, 11)
            request.session['current_gold'] += q
            print q
            request.session['log'].insert(0,('You have earned {} gold from the cave @ {}'.format(q, datetime.now())))
            return redirect('/')
        elif(request.POST['building'] == 'house'):
            q = random.randrange(2, 6)
            request.session['current_gold'] += q
            print q
            request.session['log'].insert(0,('You have earned {} gold from the house @ {}'.format(q, datetime.now())))
            return redirect('/')
        elif(request.POST['building'] == 'casino'):
            rand_int = random.randrange(1, 3)
            if(rand_int == 1):
                q = random.randrange(0, 51)
                request.session['current_gold'] += q
                request.session['log'].insert(0,('You have earned {} gold from the casino @ {}'.format(q, datetime.now())))
                return redirect('/')
            elif(rand_int == 2):
                q = random.randrange(0, 51)
                request.session['current_gold'] -= q
                request.session['log'].insert(0,('You have LOST {} gold from the casino @ {}'.format(q, datetime.now())))
                return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return render(request, 'ninja_gold/index.html')
