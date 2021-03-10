from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('share_your_ideas', views.share_your_ideas, name='share_your_ideas'),
]