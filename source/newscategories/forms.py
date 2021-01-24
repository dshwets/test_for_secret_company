from django import forms

from common.forms import AbstractCreatedByForm
from newscategories.models import Category


class CategoryCreateForm(AbstractCreatedByForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'parent_id',
            'image',
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'parent_id',
            'image',
        ]
