from django.urls import path
from . import views

# create urls template

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
