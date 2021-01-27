from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from news.models import Article


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

