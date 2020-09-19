from django.urls import path,include
from .views import article_detail,article_list


urlpatterns = [

    path('article/list/',article_list,name="article_list"),
    path('article/detail/<int:pk>',article_detail,name="article_datail"),
]
