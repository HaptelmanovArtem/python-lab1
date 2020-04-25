from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:image_id>/like/', views.like, name="like"),
    path('<int:image_id>/dislike/', views.dislike, name="dislike"),
    path('top/', views.top, name="top"),
]