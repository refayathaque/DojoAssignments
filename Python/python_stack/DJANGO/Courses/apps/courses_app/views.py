from django.shortcuts import render, HttpResponse, redirect

from .models import Course

def index(request):

    courses = Course.objects.all()

    context = {"courses": courses}

    return render(request, 'courses_app/index.html', context)

def add_course(request):

    Course.objects.create(name = request.POST['name'], description = request.POST['description'])

    return redirect('/')
