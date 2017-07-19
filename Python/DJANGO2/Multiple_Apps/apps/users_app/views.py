from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def register(request):
    response = "placeholder dor users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "placeholder to display all users"
    return HttpResponse(response)
