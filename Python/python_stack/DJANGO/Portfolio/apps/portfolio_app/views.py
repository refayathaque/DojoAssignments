from django.shortcuts import render, HttpResponse
def index(request):
    print "*"*50
    return render(request, 'portfolio_app/index.html')

def testimonials(request):
    print "*"*50
    return render(request, 'portfolio_app/testimonials.html')
