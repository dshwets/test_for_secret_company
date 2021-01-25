from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from news.models import Article


class ArticleDetailView(PermissionRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    permission_required = 'news.can_view_article'

    def has_permission(self):
        article = self.get_object()
        return super().has_permission() or article.user_id == self.request.user
