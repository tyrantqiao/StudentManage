from django.urls import path
from . import views

app_name='grades'
urlpatterns= [
    #base url is '39.108.118.***:8000/grades/'
    path('',views.index,name='index'),
    path('lists/',views.lists,name='lists'),
    path('inquire/',views.inquire,name='inquire'),
    path('details/',views.details,name='details'),
    path('manager/',views.manager,name='manager'),
]
