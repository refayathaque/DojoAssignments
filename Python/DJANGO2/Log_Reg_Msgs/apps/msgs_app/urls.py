from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log_out$', views.log_out, name='log_out'),
    # url(r'^new/$', views.new),
    url(r'^create$', views.create, name='send_message')
    # url(r'^(?P<number>\d+)/$', views.show),
    # url(r'^(?P<number>\d+)/edit$', views.edit),
    # url(r'^(?P<number>\d+)/delete$', views.destroy)
]

# 'Named Routes' implemented above
