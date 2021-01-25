from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'registration/account_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('newscategories:list_newscategory')
