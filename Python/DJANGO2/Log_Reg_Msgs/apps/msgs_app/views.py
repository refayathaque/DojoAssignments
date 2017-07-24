from django.shortcuts import render, redirect

def index(request):
    return render(request, 'msgs_app/index.html')
