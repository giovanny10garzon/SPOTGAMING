from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_page, name='index'),
    path('sistemagestionsg/', views.pagina_inicial, name='sistemagestionsg'),
]