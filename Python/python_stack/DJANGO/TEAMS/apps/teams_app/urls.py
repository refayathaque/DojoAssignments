from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^make_team$', views.make_team),
    url(r'^join_team$', views.join_team),
    url(r'^return_to_index$', views.return_to_index),
    url(r'^team_listings$', views.team_listings),
    url(r'^user_information/(?P<last_name>\w+)$', views.user_information),
    url(r'^leave_team/(?P<team_name>\w+\s\w+)$', views.leave_team) # Imp REGEX for things with spaces in between like 'Monitor FC'
]
