# How to start Django Projects...

# 1. django-admin startproject <name of your project>
    # this line must be executed in the folder where you want to have the project,
    # don't do 'mkdir <name of your project>'!

# 2. mkdir apps
    # this must be done INSIDE the project folder Django just created for you

# 3. touch __init__.py
    # this must be done INSIDE the 'apps' folder you just made in previous step

# 4. python ../manage.py startapp <name of your app>
    # this must be done INSIDE the 'apps' folder

# 5. open 'settings.py', it's within the <name of your project> folder
    # add to the INSTALLED_APPS list 'apps.<name of your app>',

# 6. python manage.py runserver
    # run localhost:8000 to make sure set up is working thus far

# 7. open 'urls.py', it's within the <name of your project> folder
    # modify to look like this:
    from django.conf.urls import url, include
    from django.contrib import admin
    urlpatterns = [
        url(r'^', include('apps.<name of your app>.urls'))
    ]

# 8. touch urls.py
    # this must be done INSIDE the <name of your app> folder, which in turn is
    # within the 'apps' folder

# 9. open 'urls.py' just created above
    # add these lines:
    from django.conf.urls import url
    from . import views
    urlpatterns = [
        url(r'^$', views.index)
        # url(r'^<second route>$', views.<second route>)
            # ^ format for more than one route (anything other than index)
    ]

# 10. open 'views.py' within the <name of your app> folder
    # add these lines:
    from django.shortcuts import render, HttpResponse
    def index(request):
        print "*"*50
        return render(request, '<name of your app>/index.html')

# 11. touch index.html
    # this must be done here:
    # |_apps
	  # |_yourapp
		# |_templates
	      # |_yourapp
		    # |_index.html
			  # |_showusers.html

# 12. python manage.py runserver
    # run localhost:8000 again to make sure everything is working

################################################################################

# STATIC FILES

 <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title></title>
        {% load staticfiles %}
      <!-- The line above tells Django to be ready to listen for static files -->
      <link rel="stylesheet" href="{% static 'ourApp/css/main.css' %}"media="screen" title="no title"  charset="utf-8">
      </head>
    <body>
    </body>
  </html>

 # CSRF TOKEN

<form action="/new_user" method="post">
	{% csrf_token %}
	<input type="text" name="first_name">
	<input type="submit" value="submit">
</form>

# POST/GET LOGIC

from django.shortcuts import render, redirect
def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.method
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")
