from blog_app import views
from django.urls import path
from django.conf import settings


app_name='blog_app'
urlpatterns = [
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('addpost',views.addpost,name='addpost'),
    path('deletepost/<id>',views.deletepost,name='deletepost'),
    path('viewpost',views.viewpost,name='viewpost'),
    path('updatepost/<id>',views.updatepost,name='updatepost'),
    path('detail/<id>',views.detailview,name='detailview'),

]
