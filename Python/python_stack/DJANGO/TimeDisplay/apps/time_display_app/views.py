from django.shortcuts import render, HttpResponse
import datetime

def index(request):
  print datetime.datetime.now()
  context = {
      'current_time': datetime.datetime.now()
      }
  return render(request,'time_display_app/index.html', context)

#datetime.datetime.now() outputs a string, so we set it as the VALUE of the
#context DICTIONARY, and we set the KEY as variable 'current_time' that we
#call using TEMPLATING on the html side
