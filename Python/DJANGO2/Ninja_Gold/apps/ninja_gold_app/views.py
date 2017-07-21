from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_gold_app/index.html')

def clear(request):
    request.session.clear()
    return redirect('/')

def process_money(request):
    dt = datetime.now().strftime('%-I:%M %p, %b %-d, %Y')
    if request.POST['place'] == 'farm':
        rand = random.randint(10, 20)
        act_data = {
            'gold' : rand,
            'place' : 'farm',
            'dt' : dt,
            'verb' : 'earned'
        }
        request.session['activities'].append(act_data)
        request.session['gold'] += rand
    elif request.POST['place'] == 'cave':
        rand = random.randint(5, 10)
        act_data = {
            'gold' : rand,
            'place' : 'cave',
            'dt' : dt,
            'verb' : 'earned'
        }
        request.session['activities'].append(act_data)
        request.session['gold'] += rand
    elif request.POST['place'] == 'house':
        rand = random.randint(2, 5)
        act_data = {
            'gold' : rand,
            'place' : 'house',
            'dt' : dt,
            'verb' : 'earned'
        }
        request.session['activities'].append(act_data)
        request.session['gold'] += rand
    elif request.POST['place'] == 'casino':
        binary = random.randint(0, 1)
        rand = random.randint(0, 50)
        if binary == 0:
            act_data = {
                'gold' : rand,
                'place' : 'casino',
                'dt' : dt,
                'verb' : 'earned'
            }
            request.session['activities'].append(act_data)
            request.session['gold'] += rand
        else:
            act_data = {
                'gold' : rand,
                'place' : 'casino',
                'dt' : dt,
                'verb' : 'lost'
            }
            request.session['activities'].append(act_data)
            request.session['gold'] -= rand
    return redirect('/')
