from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from news.forms import ArticleUpdateForm
from news.models import Article


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'article_update.html'
    form_class = ArticleUpdateForm
    model = Article
    success_url = reverse_lazy('news:article_list')
    permission_required = 'news.can_change_article'

    def has_permission(self):
        article = self.get_object()
        return super().has_permission() or article.user_id == self.request.user
