from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from newscategories.models import Category


class NewsCategoriesListView(LoginRequiredMixin, ListView):
    template_name = 'news_category_list.html'
    queryset = Category.objects.all().order_by('-pk')
    context_object_name = 'categories'
    paginate_by = 9
    paginate_orphans = 2
