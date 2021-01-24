from django.urls import reverse_lazy
from django.views.generic import CreateView

from newscategories.forms import CategoryForm
from newscategories.models import Category


class NewsCategoryCreateView(CreateView):
    template_name = 'news_category_create.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
