from django.urls import path
from . import views

app_name = 'contributions'

urlpatterns = [
    path('', views.home, name='home'),
]