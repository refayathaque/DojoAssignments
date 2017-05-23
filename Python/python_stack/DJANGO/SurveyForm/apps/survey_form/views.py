from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "*"*50
    return render(request, 'survey_form/index.html')

def data_input(request):
    if request.method == "POST": # SETTING SESSIONS!
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1
        return redirect('/result') # bc POST
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey_form/result.html')
