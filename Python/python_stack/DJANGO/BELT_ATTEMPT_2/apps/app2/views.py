from django.shortcuts import render, redirect

from .models import User, Quote, User_Quote

from django.contrib import messages

from django.db.models import Count

from sets import Set

def quotes(request):

    a = set( Quote.objects.all() ) # all quotes
    b = set( Quote.objects.filter(quote_name__user_id__email = request.session['email']).all() ) # user favorited

    all_quotes_minus_what_users_favorited = (a.difference(b))

    context = {
                'all_quotes_minus_what_users_favorited' : all_quotes_minus_what_users_favorited,
                'all_user_favorited' : User_Quote.objects.filter(user_id__email__contains = request.session['email']),
                'user_information' : User.objects.filter(email = request.session['email'])
                }

    return render(request, 'app2/quotes.html', context)

def create_quote(request):

    session = request.session['email']

    results = Quote.objects.create_quote(request.POST, session)

    if results[0]:
        return redirect('/app2/quotes')

    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/app2/quotes')

def log_out(request):
    request.session.clear()
    return redirect('/')

def display_users(request, email):

    context = {
                'users_posts' : Quote.objects.filter(posted_by = email),
                'user' : User.objects.filter(email = email),
                'count' : Quote.objects.filter(posted_by = email).count()
                }

    return render(request, 'app2/users.html', context)

def remove_from_favorites(request, quote_id__posted_by):
    User_Quote.objects.filter(user_id__email = request.session['email']).filter(quote_id__posted_by = quote_id__posted_by).delete()
    return redirect('/app2/quotes')

def add_to_favorites(request, id):

    user_object = User.objects.filter(email = request.session['email'])
    quote_object = Quote.objects.filter(id = id)
    User_Quote.objects.create(quote_id = quote_object[0], user_id = user_object[0])

    return redirect('/app2/quotes')
