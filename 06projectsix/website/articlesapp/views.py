#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "home.html"

    def get_queryset(self):
        return Article.objects.order_by("-date_added")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
    context_object_name = "blogs"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = "__all__"
