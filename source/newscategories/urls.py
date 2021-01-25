from django.urls import path

from newscategories.views.news_category_create import NewsCategoryCreateView
from newscategories.views.news_category_delete import NewsCategoryDeleteView
from newscategories.views.news_category_list import NewsCategoriesListView
from newscategories.views.news_category_update import NewsCategoryUpdateView

app_name = 'newscategories'

urlpatterns = [
    path('', NewsCategoriesListView.as_view(), name='list_newscategory'),
    path('categories/create/', NewsCategoryCreateView.as_view(), name='create_newscategory'),
    path('categories/<int:pk>/delete/', NewsCategoryDeleteView.as_view(), name='delete_newscategory'),
    path('categories/<int:pk>/update/', NewsCategoryUpdateView.as_view(), name='update_newscategory'),
]
