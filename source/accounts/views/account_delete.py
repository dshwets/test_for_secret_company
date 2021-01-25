from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from accounts.models import User


class AccountDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'account_delete.html'
    model = User
    success_url = reverse_lazy('accounts:account_list')
    context_object_name = 'account'
    permission_required = 'accounts.can_delete_user'

