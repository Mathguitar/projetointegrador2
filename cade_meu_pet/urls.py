from django.urls import path
from cade_meu_pet import views

urlpatterns = [
    path('', views.index),
    path('encontrados/', views.encontrados, name='encontrados'),
    path('perdidos/', views.perdidos, name='perdidos'),
]
