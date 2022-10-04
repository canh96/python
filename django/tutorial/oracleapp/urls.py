from django.urls import path
from . import views
app_name = 'oracle'

urlpatterns = [
    path('test/', views.test),
    path('test2/', views.test2),
    path('member_list/', views.view_Member_List),
    path('member/', views.view_Member),
    path('member_list_dict/', views.view_Member_ListDict),
    path('member_list_page/', views.Member_List_Page, name ='member_list_page'),

]