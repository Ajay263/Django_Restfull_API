
from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.eventList,name='event_list'),
    path('detail/<str:pk>/',views.eventDetail, name='event_detail'),
    path('create',views.eventCreate, name='event_create'),
    path('update/<str:pk>/',views.eventUpdate, name='event_update'),
    path('delete/<str:pk>/',views.eventDelete, name='event_delete'),
    

]






    