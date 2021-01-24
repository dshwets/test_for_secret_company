from django import forms

from newscategories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'parent_id',
            'image',
        ]
