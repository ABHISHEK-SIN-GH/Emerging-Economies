from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('errorPage',views.errorPage,name="error"),
    path('dashboard',views.dashboard,name="dashboard"),
]