from django.urls import reverse_lazy
from django.views.generic import DeleteView
from newscategories.models import Category


class NewsCategoryDeleteView(DeleteView):
    template_name = 'news_categories_delete.html'
    model = Category
    success_url = reverse_lazy('news:list_newscategories')
    context_object_name = 'category'
