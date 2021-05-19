# -*- encoding: utf-8 -*-
"""
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('createItemForm/', views.createItemForm, name='createItemForm'),
    path('createStationForm/', views.createStationForm, name='createStationForm'),
    path('createPaymentForm/', views.createPaymentForm, name='createPaymentForm'),
    path('createSMSForm/', views.createSMSForm, name='createSMSForm'),


    path('resentSMS/', views.createSMSForm, name='resendSMS'),
    


    path('showItem/<id>/', views.showItem, name='showItem'),
    # edit Items
    path('editItem/<id>/', views.editItem, name='editItem'),


    path('getItem/<id>/delete', views.deleteItem, name='deleteItem'),
    
    # url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
