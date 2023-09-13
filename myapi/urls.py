from django.urls import include, path
from rest_framework import routers
from  .views import *

urlpatterns = [
     path('heroes/', HeroDetails.as_view()),
     path('heroes/<int:hero_id>/',HeroDetail.as_view()),
     path('heroes/add/', AddHero.as_view()),
     path('heroes/delete/<int:hero_id>/', DeleteHero.as_view()),
     path('heroes/delete/', DeleteHeroes.as_view()),
     path('heroes/update/<int:hero_id>/',UpdateHero.as_view())
]