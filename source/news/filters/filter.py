import django_filters
from django.db.models import Q
from django import forms

from news.models import Article


class ArticleSearch(django_filters.FilterSet):
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
        model = Article
        fields = ['search']

    def names_filter(self, queryset, _name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(user_id__username__icontains=value)
        )
