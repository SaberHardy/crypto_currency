from django.urls import path
from positions import views

urlpatterns = [
    path('', views.home, name='home'),
]
