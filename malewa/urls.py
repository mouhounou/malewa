from django.urls import path
from . import views

app_name = 'malewa'

urlpatterns = [
    path('plats', views.plats, name='plats'),
]
