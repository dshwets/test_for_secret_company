from django import forms

from accounts.models import User


class AbstractCreatedByForm(forms.ModelForm):
    """Your model must be inherited from 'AbstractCreatedByModel',
        also you must inherit your view which will works with this form
         from 'CreatedByCreateView',
         or you can use it with models and views where those fields are exists"""
    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('created_by', None)
        created_by = User.objects.get(pk=user_pk)
        self.created_by = created_by
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        form = super().save(commit=False)
        form.created_by = self.created_by
        if commit:
            form.save()
        return form
