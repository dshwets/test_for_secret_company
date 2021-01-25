from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from common.views.created_by_create_view import CreatedByCreateView
from newscategories.forms import CategoryCreateForm
from newscategories.models import Category


class NewsCategoryCreateView(PermissionRequiredMixin, CreatedByCreateView):
    template_name = 'news_category_create.html'
    form_class = CategoryCreateForm
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
    permission_required = 'newscategories.can_add_category'