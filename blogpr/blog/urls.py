from django.urls import path
from .views import hello, index, post_list, post_detail, post_create


urlpatterns = [
    path('hello/',hello),
    path('index/', index, name = 'index'),
    path('',post_list, name ='list'),
    path('detail/<int:id>/',post_detail, name ='detail'),
    path('create/', post_create, name ='create'),
]
