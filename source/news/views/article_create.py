from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from common.views.created_by_create_view import CreatedByCreateView
from news.forms import ArticleCreateForm
from news.models import Article


class ArticleCreateView(PermissionRequiredMixin, CreatedByCreateView):
    template_name = 'article_create.html'
    form_class = ArticleCreateForm
    model = Article
    success_url = reverse_lazy('news:article_list')
    permission_required = 'news.can_add_article'
