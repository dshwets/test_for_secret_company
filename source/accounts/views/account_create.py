from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm
from accounts.models import User


class RegisterView(CreateView):
    model = User
    template_name = 'account_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('newscategories:list_newscategory')
