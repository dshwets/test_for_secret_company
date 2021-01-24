from django.urls import path

from newscategories.views.news_categories_list import NewsCategoriesListView

app_name = 'news'

urlpatterns = [
    path('categories/', NewsCategoriesListView.as_view(), name='list_newscategories'),
]
