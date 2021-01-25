from django.urls import path


from news.views.article_list import ArticleListView

app_name = 'news'

urlpatterns = [
    path('news/', ArticleListView.as_view(), name='article_list'),
    path('categories/<int:pk>/news', ArticleListView.as_view(), name='article_category_list')
]
