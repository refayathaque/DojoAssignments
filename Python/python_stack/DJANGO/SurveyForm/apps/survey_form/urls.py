from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^data_input$', views.data_input),
    url(r'^result$', views.result)
]
