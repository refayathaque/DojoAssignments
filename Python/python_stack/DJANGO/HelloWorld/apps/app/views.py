from django.shortcuts import render

# Create your views here.
# the index function is called when root is visited
def index(request):
    print 'hello world'
    return render(request, 'app/index.html')
