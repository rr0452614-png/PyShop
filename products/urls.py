from django.urls import path
from . import views


urlpatterns=[                     #ignore errors here
    path('', views.index),
    path('new', views.new)
]