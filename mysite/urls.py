from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('result', views.result, name='result'),
]