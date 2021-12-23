from .views import *
from django.urls import path,include
urlpatterns = [
    path('', index),
    path('blogs', blogs,name='blogs'),
    path('blog/<slug:url>', blog),
]
#0ba26d8c-f2aa-49a9-8d3d-b1bb64705641