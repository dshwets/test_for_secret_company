from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from newscategories.forms import CategoryForm
from newscategories.models import Category


class NewsCategoryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'news_category_update.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
    permission_required = 'newscategories.can_change_category'

    def has_permission(self):
        category = self.get_object()
        return super().has_permission() or category.created_by == self.request.user
