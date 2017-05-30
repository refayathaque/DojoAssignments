from django.shortcuts import render, HttpResponse, redirect

from .models import User, Trip, User_Trip

from django.contrib import messages

def travels(request):

    if request.session['logged_in_user_username']:

        a = set( Trip.objects.all() ) # all trips
        b = set( Trip.objects.filter(trip_name__user_id__username = request.session['logged_in_user_username']).all() ) # user trips

        all_trips_minus_what_users_are_part_of = (a.difference(b))

        context = {
                    'all_trips_minus_what_users_are_part_of' : all_trips_minus_what_users_are_part_of,
                    'all_trips' : Trip.objects.all(),
                    'all_user_trips' : User_Trip.objects.filter(user_id__username__contains = request.session['logged_in_user_username']),
                    'user_information' : User.objects.filter(username = request.session['logged_in_user_username'])
                    }

    elif request.session['registered_user_username']:

        a = set( Trip.objects.all() ) # all trips
        b = set( Trip.objects.filter(trip_name__user_id__username = request.session['registered_user_username']) ) # user trips

        all_trips_minus_what_users_are_part_of = (a.difference(b))

        context = {
                    'all_trips_minus_what_users_are_part_of' : all_trips_minus_what_users_are_part_of,
                    'all_trips' : Trip.objects.all(),
                    'all_user_trips' : User_Trip.objects.filter(user_id__username__contains = request.session['registered_user_username']),
                    'user_information' : User.objects.filter(username = request.session['registered_user_username'])
                    }

    return render(request, 'app2/travels.html', context)

def make_trip(request):

    results = Trip.objects.make_trip(request.POST)

    if results[0]:

        # Adds user to the trip they just made
        if request.session['logged_in_user_username']:

            user_object = User.objects.filter(username = request.session['logged_in_user_username'])
            trip_object = Trip.objects.filter(destination = request.POST['destination'])
            User_Trip.objects.create(trip_id = trip_object[0], user_id = user_object[0])

        elif request.session['registered_user_username']:

            user_object = User.objects.filter(username = request.session['registered_user_username'])
            trip_object = Trip.objects.filter(destination = request.POST['destination'])
            User_Trip.objects.create(trip_id = trip_object[0], user_id = user_object[0])

        return redirect('/travels')

    else:

        for err in results[1]:
            messages.error(request, err)

        return redirect('/add')
####

def join_trip(request, destination):

    if request.session['logged_in_user_username']:

        user_object = User.objects.filter(username = request.session['logged_in_user_username'])
        trip_object = Trip.objects.filter(destination = destination)
        User_Trip.objects.create(trip_id = trip_object[0], user_id = user_object[0])

        return redirect('/travels')

    elif request.session['registered_user_username']:

        user_object = User.objects.filter(username = request.session['registered_user_username'])
        trip_object = Trip.objects.filter(destination = destination)
        User_Trip.objects.create(trip_id = trip_object[0], user_id = user_object[0])

        return redirect('/travels')

def display_trip(request, destination):

    context = {
                'trip' : Trip.objects.filter(destination = destination),
                'other_users_in_trip' : User.objects.filter(user_name__trip_id__destination = destination)
                }

    return render(request, 'app2/destination.html', context)

def add(request):
    return render(request, 'app2/add.html')

def log_out(request):
    return render(request, 'app1/index.html')
