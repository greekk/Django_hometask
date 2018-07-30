from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('contacts', views.contacts, name='contacts'),
    path('<int:pk>/', views.details, name='details'),

]