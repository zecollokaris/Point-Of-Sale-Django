from django.urls import path
''' 
This is to allow us to connect the PROJECT's  url with this APP's url 
it will then allow us to define paths here as we had included (Management urls)
in the PROJECT.
'''

from django.conf.urls import url,include

from Management import views
'''
Here we are importing the views as we shall connect templates from there 
'''


from django.contrib import admin

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [



#################################################################################################################################################################################
#URL FOR  HOME PAGE
#################################################################################################################################################################################

    #HOME Page url!

    #This is the home page url pattern 
    path('', views.index, name= 'index'),

#################################################################################################################################################################################
#URL FOR LIST OF ITEMS PAGE VIEW FUNCTION
#################################################################################################################################################################################

    #LIST OF ITEMS Page url!

    #This is the List of Items page url pattern 
    path('list_items/', views.list_items, name='list_items'),

#################################################################################################################################################################################
#URL FOR ADD ITEMS PAGE VIEW FUNCTION
#################################################################################################################################################################################

    #ADD ITEMS Page url!

    #This is the Add Items page url pattern 
    path('add_items/', views.add_items, name='add_items'),

#################################################################################################################################################################################
#URL FOR STOCK DETAIL PAGE VIEW FUNCTION
#################################################################################################################################################################################

    #Stock Detail Page url!

    #This is Display Sock Item url pattern
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),

#################################################################################################################################################################################
#URL FOR ISSUE ITEM PAGE VIEW FUNCTION
#################################################################################################################################################################################

    #Issue Item Page url!

    #This is Issue Item url pattern
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    
#################################################################################################################################################################################
#URL FOR RECEIVE ITEM PAGE VIEW FUNCTION
#################################################################################################################################################################################

    #Receive Item Page url!

    #This is Receive Item url pattern
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),

]
