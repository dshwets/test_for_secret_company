from django.urls import path

from news.views.article_create import ArticleCreateView
from news.views.article_detail import ArticleDetailView
from news.views.article_list import ArticleListView

app_name = 'news'

urlpatterns = [
    path('news/', ArticleListView.as_view(), name='article_list'),
    path('news/create/', ArticleCreateView.as_view(), name='article_create'),
    path('news/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('categories/<int:pk>/news', ArticleListView.as_view(), name='article_category_list'),
]
