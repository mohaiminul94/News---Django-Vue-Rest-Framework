from django.urls import path
from news.api.views import (ArticleDetailAPIView, ArticleListCreateAPIView)

urlpatterns = [
    path("articles/", 
         ArticleListCreateAPIView.as_view(), 
         name="article-list"),

    path("articles/<int:pk>/", 
         ArticleDetailAPIView.as_view(), 
         name="article-detail")
]