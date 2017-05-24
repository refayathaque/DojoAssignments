from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "*"*50
    return render(request, 'disappearing_ninjas/index.html')

def ninjas(request):
    print "*"*50
    return render(request, 'disappearing_ninjas/ninjas.html')

def show(request, color):
    print "*"*50
    context = { "color" : color }
    return render(request, 'disappearing_ninjas/show.html', context)
