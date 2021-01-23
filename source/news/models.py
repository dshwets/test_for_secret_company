from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    category_id = models.ForeignKey(
        'newscategories.Category',
        related_name='articles',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Категория'),
    )

    user_id = models.ForeignKey(
        'accounts.User',
        related_name='articles',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Автор'),
    )

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name=_('Заголовок'),
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name=_('Текст статьи'),
    )

    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_('Изображение'),
    )

    def __str__(self):
        return f'{self.title}'[0:100]

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

        permissions = [
            ('can_add_article', _('Может добавлять статьи')),
            ('can_change_article', _('Может изменять статьи')),
            ('can_delete_article', _('Может удалять статьи')),
            ('can_view_article', _('Может просматривать статьи')),
        ]
