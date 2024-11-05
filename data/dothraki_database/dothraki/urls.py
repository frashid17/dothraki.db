from django.urls import path
from . import views

urlpatterns = [
    path('dothraki/',views.members,name='members')
]