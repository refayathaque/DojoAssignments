from django.shortcuts import render, redirect

from .models import User, Team, User_Team

from django.contrib import messages

def success(request):
    context = {
                'all_teams' : Team.objects.all()
                'all_user_teams' : Team_User.objects.filter(email = request.session['something'])
    }
    return render(request, 'teams_app/success.html', context)

def make_team(request):
    results = Team.objects.make_team(request.POST)
    if results[0]:
        return redirect('/success')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/success')

def join_team(request):
    if request.session['logged_in_user_object']:
        user_object = User.objects.filter(email = request.session['logged_in_user_object'])
    elif request.session['registered_user_object']:
        user_object = User.objects.filter(email = request.session['registered_user_object'])
    team_object = Team.objects.filter(name = request.POST['team_join'])

    Team_User.objects.create(team_id = team_object[0], user_id = user_object[0])
