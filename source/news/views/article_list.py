from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

from news.filters.filter import ArticleSearch
from news.models import Article


class ArticleListView(LoginRequiredMixin, FilterView):
    template_name = 'article_list.html'
    filterset_class = ArticleSearch
    context_object_name = 'articles'
    paginate_by = 9
    paginate_orphans = 2

    def get_queryset(self):
        if self.kwargs:
            return Article.objects.filter(category_id=self.kwargs['pk']).order_by('-pk')
        else:
            return Article.objects.all().order_by('-pk')
