from django.urls import path
from .views import home,blogViewPage,like,addComment,categoryFilter,search,addReader
urlpatterns=[
    path('',home,name='home'),
    path('posts/<str:slug>',blogViewPage,name='posts'),
    path('like/<str:slug>',like),
    path('comment/<str:slug>',addComment),
    path('categories/<str:category>',categoryFilter),
    path('search/',search),
    path('addemail',addReader,name='addemail'),
]