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
    url(r'^remove_from_favorites/(?P<id>\d+)$', views.remove_from_favorites),
    url(r'^add_to_favorites/(?P<id>\d+)$', views.add_to_favorites)
]

# urlpatterns = [
#     url(r'^travels$', views.travels),
#     url(r'^make_trip$', views.make_trip),
#     url(r'^add$', views.add),
#     url(r'^join_trip/(?P<destination>\w+)$', views.join_trip),
#     url(r'^join_trip/(?P<destination>\w+\s\w+)$', views.join_trip),
#     url(r'^display_trip/(?P<destination>\w+)$', views.display_trip),
#     url(r'^display_trip/(?P<destination>\w+\s\w+)$', views.display_trip),
#     url(r'^log_out$', views.log_out)
# ]
