from django.shortcuts import render, HttpResponse, redirect

def index(request):
    try:
        del request.session['name']
        del request.session['dojo_location']
        del request.session['favorite_language']
        del request.session['key']
    except:
        pass

    return render(request, 'survey_form/index.html')

def process(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    return render(request, 'survey_form/result.html')
