from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name='about'),
    path('sign', views.sign, name='sign'),
    path('register', views.register, name='register'),
    path('story', views.story, name='story')
]

