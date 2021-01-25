from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label=_('Псевдоним'))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]


class MyUserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=_('Псевдоним'))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
