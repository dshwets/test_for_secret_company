from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


class CreatedByCreateView(LoginRequiredMixin, CreateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['created_by'] = self.request.user.pk
        return kwargs
