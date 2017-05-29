from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^make_team$', views.make_team),
    url(r'^join_team$', views.join_team),
    url(r'^return_to_index$', views.return_to_index),
    url(r'^team_listings$', views.team_listings)
]
