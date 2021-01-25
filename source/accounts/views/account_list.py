from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from accounts.models import User


class AccountListView(PermissionRequiredMixin, ListView):
    template_name = 'account_list.html'
    queryset = User.objects.all().order_by('-pk')
    context_object_name = 'accounts'
    permission_required = 'accounts.can_view_user'
    paginate_by = 9
    paginate_orphans = 2
