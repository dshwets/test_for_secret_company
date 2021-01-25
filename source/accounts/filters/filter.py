import django_filters
from django.db.models import Q
from django import forms

from accounts.models import User


class UserSearch(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='names_filter',
        label='',
        widget=forms.TextInput(
            attrs={
                'class': "form-control mr-sm-2"
            }
        )
    )

    class Meta:
        model = User
        fields = ['search']

    def names_filter(self, queryset, _name, value):
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value) |
            Q(username__icontains=value)
        )
