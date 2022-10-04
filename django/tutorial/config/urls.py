from django.contrib import admin
from django.urls import include, path
from firstapp import views as fv
from secondapp import views as sv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', fv.index1),
    path('index2/', fv.index2),
    path('first/', include('firstapp.urls')),
    path('second/', include('secondapp.urls')),
    path('oracle/', include('oracleapp.urls')),
    path('frontend/', include('frontendapp.urls')),
    path('db/', include('dbapp.urls')),
    path('chi2/', include('chi2app.urls')),
]
