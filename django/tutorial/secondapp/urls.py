from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('oneshow/', views.oneshow),
    path('show2/', views.show2),
    path('lprod_list/', views.view_Lprod_List),
    path('lprod/', views.view_Lprod),
]
