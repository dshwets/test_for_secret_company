from django.urls import path

from newscategories.views.news_categories_create import NewsCategoryCreateView
from newscategories.views.news_categories_delete import NewsCategoryDeleteView
from newscategories.views.news_categories_list import NewsCategoriesListView
from newscategories.views.news_categories_update import NewsCategoryUpdateView

app_name = 'news'

urlpatterns = [
    path('categories/', NewsCategoriesListView.as_view(), name='list_newscategories'),
    path('categories/create/', NewsCategoryCreateView.as_view(), name='create_newscategories'),
    path('categories/<int:pk>/delete/', NewsCategoryDeleteView.as_view(), name='delete_newscategories'),
    path('categories/<int:pk>/update/', NewsCategoryUpdateView.as_view(), name='update_newscategories'),
]
