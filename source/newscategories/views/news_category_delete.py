from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from newscategories.models import Category


class NewsCategoryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'news_category_delete.html'
    model = Category
    success_url = reverse_lazy('newscategories:list_newscategory')
    context_object_name = 'category'
    permission_required = 'newscategories.can_delete_category'

    def has_permission(self):
        category = self.get_object()
        return super().has_permission() or category.created_by == self.request.user
