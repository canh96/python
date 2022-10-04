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
    path('sample01/', views.sample_01),
    path('index01/', views.index_01),
    path('index_css02/', views.index_02),
    path('index_css03/', views.index_03),
    path('index_css04/', views.index_04),
    path('index_css05/', views.index_05),
    path('index_css06/', views.index_06),
    path('test/', views.view_Test),
    path('dbtest/', views.view_DB_Test),
    path('CreateTable/', views.CreateTable),
    path('insert_test/', views.set_Survey_Insert_test),
    path('survey_list/', views.view_Survey_List),
    path('survey/', views.view_Servey),
    path('insert/', views.set_Survey_Insert),
    path('analysis/', views.survey_Analysis),
]
