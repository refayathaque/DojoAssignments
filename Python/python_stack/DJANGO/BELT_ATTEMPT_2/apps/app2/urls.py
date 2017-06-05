from django.conf.urls import url

from . import views

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

full_name = re.compile(r'^([a-z A-Z])*$')

urlpatterns = [
    url(r'^quotes$', views.quotes),
    url(r'^display_users/([a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)$', views.display_users),
    url(r'^display_users/([a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)$', views.display_users),
    url(r'^create_quote$', views.create_quote),
    url(r'^log_out$', views.log_out),
    url(r'^remove_from_favorites/([a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)$', views.remove_from_favorites),
    url(r'^add_to_favorites/(?P<id>\d+)$', views.add_to_favorites)
]
