from django.contrib.auth.mixins import PermissionRequiredMixin
from django_filters.views import FilterView

from accounts.filters.filter import UserSearch
from accounts.models import User


class AccountListView(PermissionRequiredMixin, FilterView):
    template_name = 'account_list.html'
    queryset = User.objects.all().order_by('-pk')
    filterset_class = UserSearch
    context_object_name = 'accounts'
    permission_required = 'accounts.can_view_user'
    paginate_by = 9
    paginate_orphans = 2

