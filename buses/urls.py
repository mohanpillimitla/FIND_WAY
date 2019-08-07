from django.contrib import admin
from django.urls import path,include
from .views import displaybuses,findLocation

urlpatterns = [
    path('bus/<int:id>/',displaybuses,name='displaybuses'),
    path('',findLocation,name='location')
]
