from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="blogpage"),
    path("article/new/", views.ArticleCreateView.as_view(), name="new_article"),
    path("article/<int:pk>/edit",
         views.ArticleUpdateView.as_view(), name="article_edit"),
]
