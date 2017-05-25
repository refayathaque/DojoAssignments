from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index),

    url(r'^add_course$', views.add_course),

    url(r'^remove/(?P<aidee>\d+)$', views.remove),

    url(r'^delete_course/(?P<aidee>\d+)$', views.delete_course),

    url(r'^reset$', views.reset)
]
