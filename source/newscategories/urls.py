from django.urls import path

from newscategories.views.news_categories_create import NewsCategoryCreateView
from newscategories.views.news_categories_list import NewsCategoriesListView

app_name = 'news'

urlpatterns = [
    path('categories/', NewsCategoriesListView.as_view(), name='list_newscategories'),
    path('categories/create/', NewsCategoryCreateView.as_view(), name='create_newscategories'),
]
