from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'ninja_gold_app/index.html')

def process_money(request):
    if request.POST['place'] == 'farm':
        print 'FARM', random.randint(10, 20)
    if request.POST['place'] == 'cave':
        print 'CAVE', random.randint(5, 10)
    if request.POST['place'] == 'house':
        print 'HOUSE', random.randint(2, 5)
    if request.POST['place'] == 'casino':
        print 'CASINO', random.randint(0, 50)
    return redirect('/')
