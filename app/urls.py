from xml.etree.ElementInclude import include
from django.urls import path
from .views import dashboard_view,user_view

app_name = 'app'

urlpatterns = [
 path('dashboard/', dashboard_view, name = "dashboard"),   
 path('botones/', user_view, name='botones'),


]