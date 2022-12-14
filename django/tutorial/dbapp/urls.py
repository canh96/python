from django.urls import path
from . import views
app_name = 'db'


urlpatterns = [
    path('cart_list/', views.view_Cart_List),
    path('cart/', views.view_Cart),
    path('cart_insert_form/', views.view_Cart_Insert),
    path('cart_insert/', views.set_Cart_Insert),
    path('testdict/', views.testDict),
    path('cart_list_dict/', views.view_Cart_List_dict),
    path('cart_delete/', views.set_Cart_Delete),
    path('cart_update_form/', views.view_Cart_Update),
    path('cart_update/', views.set_Cart_Update),
    path('login_form/', views.login_form),
    path('login/', views.getlogin),
    path('logout/', views.set_Logout),
    path('cart_list_page/', views.view_Cart_List_Page, name ='cart_list_page'),
    
]