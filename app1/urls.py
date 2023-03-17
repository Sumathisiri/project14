from django.urls import path
from app1.views import * 
app_name='happy'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('suesh/',suresh,name='suresh'),
 ]