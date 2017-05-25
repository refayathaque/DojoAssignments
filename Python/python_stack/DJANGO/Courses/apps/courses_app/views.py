from django.shortcuts import render, HttpResponse, redirect

from .models import Course

def index(request):

    courses = Course.objects.all()

    context = {"courses": courses}

    return render(request, 'courses_app/index.html', context)

def add_course(request):

    Course.objects.create(name = request.POST['name'], description = request.POST['description'])

    return redirect('/')

def remove(request, aidee):

    context = {"information" : Course.objects.filter(id = aidee)}

    return render(request, 'courses_app/destroy.html', context)

def delete_course(request, aidee):

    Course.objects.filter(id = aidee).delete()

    return redirect('/')

def reset(request):

    return redirect('/')
