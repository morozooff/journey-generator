from django.urls import path
from . import views

# travel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_form, name='travel_form'),
    path('waiting/<int:request_id>/', views.waiting, name='waiting'),
    path('check_status/<int:request_id>/', views.check_status, name='check_status'),
    path('result/<int:request_id>/', views.result, name='result'),
    path('profile/', views.profile, name='profile'),
]