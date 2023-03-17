from django.urls import path
from app2.views import * 
app_name='sad'
urlpatterns=[
    path('siri/',siri,name='siri'),
    path('srujju/',srujju,name='srujju'),
 ]