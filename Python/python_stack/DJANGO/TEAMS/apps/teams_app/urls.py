from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^make_team$', views.make_team)
]
