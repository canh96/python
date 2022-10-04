from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('home/', views.home),
    path('insert/', views.insert),
    path('show/', views.show),
    path('oneshow/', views.oneshow),
    path('show2/', views.show2),
    path('show3/', views.show3),
    path('show4/', views.show4),
    path('update/', views.update),
    path('delete/', views.delete),
]
