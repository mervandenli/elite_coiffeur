from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('price/', views.price, name='price'),
]