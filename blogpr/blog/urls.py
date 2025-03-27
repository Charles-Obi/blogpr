from django.urls import path
from .views import index, post_list, post_detail, post_create, post_update, post_delete, user_login


urlpatterns = [
    path('index/', index, name = 'index'),
    path('',post_list, name ='list'),
    path('detail/<int:id>/',post_detail, name ='detail'),
    path('update/<int:id>/',post_update, name ='update'),
    path('delete/<int:id>/',post_delete, name ='delete'),
    path('create/', post_create, name ='create'),
    path('login/', user_login, name ='login'),
    
]
