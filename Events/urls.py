from django.urls import path
from . import views

app_name = 'Events'
urlpatterns = [
 path('', views.view_that_returns_pdf, name='view_that_returns_pdf'),
]