from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('choose',views.choose,name='choose'),
    path('shop',views.shop)]