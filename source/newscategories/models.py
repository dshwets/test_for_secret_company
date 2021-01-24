from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название'),
    )
    parent_id = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name=_('Родительская Категория'),
        on_delete=models.SET_NULL,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_('Изображение'),
        upload_to='category_images',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

        permissions = [
            ('can_add_category', _('Может добавлять категории')),
            ('can_change_category', _('Может изменять категории')),
            ('can_delete_category', _('Может удалять категории')),
            ('can_view_category', _('Может просматривать категории')),
        ]
