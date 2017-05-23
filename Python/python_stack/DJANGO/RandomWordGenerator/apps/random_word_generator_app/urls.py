from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^randomwordgenerator$', views.random_word_generator)
]

# url(r'^randomwordgenerator$', views.random_word_generator)

# randomwordgenerator is the route (action in html), and
# random_word_generator is one of the functions in views
