from django.shortcuts import render, HttpResponse, redirect

from .models import User, Friendships

def index(request):
    context = {
        "all_users" : User.objects.all(),
        "all_friends" : Friendships.objects.all()
        }
    return render(request, 'friends_app/index.html', context)
    # Passing in objects from tables User and Friendships to display on index

def process_user(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    return redirect('/')

def build_friendship(request):
    f1 = User.objects.filter(id = request.POST['friend_1'])
    f2 = User.objects.filter(id = request.POST['friend_2'])
    # Returning a LIST with OBJECTS that MATCH the filter requirement

    Friendships.objects.create(friend1 = f1[0], friend2 = f2[0])
    # Accessing LIST's index 0 (which is the FIRST OBJECT) and assigning it to friend1 in FRIENDSHIPS

    return redirect('/')
