from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index)
    # url(r'^<second route>$', views.<function for second route>)
        # ^ format for more than one route (anything other than index)
]
