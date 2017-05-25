from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_user$', views.process_user),
    url(r'^build_friendship$', views.build_friendship)
]
