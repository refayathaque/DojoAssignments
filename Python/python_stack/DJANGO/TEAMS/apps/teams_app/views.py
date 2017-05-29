from django.shortcuts import render, redirect

from .models import User, Team, User_Team

from django.contrib import messages

from sets import Set

# SUCCESS
def success(request):
    if request.session['logged_in_user_email']:

        a = set( Team.objects.all() ) # all teams
        b = set( Team.objects.filter(team_name__user_id__email = request.session['logged_in_user_email']) ) # user teams

        all_teams_minus_what_users_are_part_of = (a.difference(b))

        context = {
                    'all_teams_minus_what_users_are_part_of' : all_teams_minus_what_users_are_part_of,
                    'all_teams' : Team.objects.all(),
                    'all_user_teams' : User_Team.objects.filter(user_id__email__contains = request.session['logged_in_user_email'])
                    }
    elif request.session['registered_user_email']:

        a = set( Team.objects.all() ) # all teams
        b = set( Team.objects.filter(team_name__user_id__email = request.session['registered_user_email']) ) # user teams

        all_teams_minus_what_users_are_part_of = (a.difference(b))

        context = {
                    'all_teams_minus_what_users_are_part_of' : all_teams_minus_what_users_are_part_of,
                    'all_teams' : Team.objects.all(),
                    'all_user_teams' : User_Team.objects.filter(user_id__email__contains = request.session['registered_user_email'])
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
        ####

def join_team(request):
    results = Team.objects.join_team(request.POST)
    if results[0]:
        if request.session['logged_in_user_email']:
            user_object = User.objects.filter(email = request.session['logged_in_user_email'])
            team_object = Team.objects.filter(id = request.POST['team_join'])
            User_Team.objects.create(team_id = team_object[0], user_id = user_object[0])
            return redirect('/success')
        elif request.session['registered_user_email']:
            user_object = User.objects.filter(email = request.session['registered_user_email'])
            team_object = Team.objects.filter(id = request.POST['team_join'])
            User_Team.objects.create(team_id = team_object[0], user_id = user_object[0])
            return redirect('/success')
    else:
        for err in results[1]: # (False, errors)
            messages.error(request, err)
        return redirect('/success')
    ####

def return_to_index(request):
    return render(request, 'login_registration_app/index.html')

# TEAM LISTINGS
def team_listings(request):
    if request.session['logged_in_user_email']:
        context = {
                    'all_teams' : Team.objects.all(),
                    'all_user_teams' : User_Team.objects.filter(team_id__name=request.POST['team_to_show'])
                    }
    elif request.session['registered_user_email']:
        context = {
                    'all_teams' : Team.objects.all(),
                    'all_user_teams' : User_Team.objects.filter(team_id__name=request.POST['team_to_show'])
                    }
    return render(request, 'teams_app/team_listings.html', context)
####

# USER INFORMATION
def user_information(request, last_name):
    context = {
        'user_information' : User.objects.filter(last_name=last_name),
        'all_user_teams' : User_Team.objects.filter(user_id__last_name__contains = last_name)
        }
    return render(request, 'teams_app/user_information.html', context)
####
