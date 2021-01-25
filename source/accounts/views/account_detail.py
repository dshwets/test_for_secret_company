from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from accounts.models import User


class AccountDetailView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'account_detail.html'
    context_object_name = 'account'
    permission_required = 'accounts.can_view_user'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user
