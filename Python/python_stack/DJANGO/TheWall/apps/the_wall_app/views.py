from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "*"*50
    return render(request, 'the_wall_app/index.html')
