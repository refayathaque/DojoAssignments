from django.shortcuts import render
from time import strftime
from datetime import datetime

def index(request):
    context = {
        "date_time" : datetime.now().strftime("%b %d, %Y, %I:%M %p")
    }
    return render(request, 'time_display/index.html', context)
