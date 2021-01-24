from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from newscategories.forms import CategoryForm
from newscategories.models import Category


class NewsCategoryUpdateView(UpdateView):
    template_name = 'news_category_update.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
