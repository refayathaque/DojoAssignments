from django.shortcuts import render

def index(request):
    print "*"*50
    return render(request, 'the_real_portfolio_app/index.html')

def projects(request):
    print "*"*50
    return render(request, 'the_real_portfolio_app/projects.html')

def about(request):
    print "*"*50
    return render(request, 'the_real_portfolio_app/about.html')

def testimonials(request):
    print "*"*50
    return render(request, 'the_real_portfolio_app/testimonials.html')
