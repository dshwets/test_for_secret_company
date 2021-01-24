from django.urls import reverse_lazy
from django.views.generic import DeleteView
from newscategories.models import Category


class NewsCategoryDeleteView(DeleteView):
    template_name = 'news_category_delete.html'
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
    context_object_name = 'category'
