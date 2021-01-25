from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from accounts.forms import MyUserUpdateForm
from accounts.models import User


class AccountUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'account_update.html'
    form_class = MyUserUpdateForm
    model = User
    permission_required = 'accounts.can_change_user'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user

    def get_success_url(self):
        return reverse('accounts:account_detail', kwargs={'pk': self.object.pk})
