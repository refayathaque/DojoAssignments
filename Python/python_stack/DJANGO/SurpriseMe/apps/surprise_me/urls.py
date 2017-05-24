from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^number_input$', views.number_input),
    url(r'^results$', views.results)
]
