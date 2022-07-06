from xml.etree.ElementInclude import include
from django.urls import path
from .import views


urlpatterns = [
    path('', views.stanishka, name = "stanishka" ),
    path('about/', views.About.as_view() )
    
]

