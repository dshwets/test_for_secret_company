from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from news.models import Article


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('news:article_list')
    context_object_name = 'article'
    permission_required = 'news.can_delete_article'
