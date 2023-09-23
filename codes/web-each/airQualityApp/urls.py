from . import views
from django.urls import path

urlpatterns = [
    path("gallery", views.gallery, name="gallery"),
    path('air', views.air, name="air"),
    path('', views.home, name="home"),
    path('mission', views.mission, name='mission'),
    path('news', views.email, name='email')
]