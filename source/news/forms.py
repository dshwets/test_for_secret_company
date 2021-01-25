from django import forms

from common.forms import AbstractCreatedByForm
from news.models import Article


class ArticleCreateForm(AbstractCreatedByForm):
    class Meta:
        fields = [
            'category_id',
            'title',
            'description',
            'image',
        ]
        model = Article

    def save(self, commit=True):
        form = super().save(commit=False)
        form.user_id = self.created_by
        if commit:
            form.save()
        return form


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'category_id',
            'title',
            'description',
            'image',
        ]