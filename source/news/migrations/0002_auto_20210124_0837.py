# Generated by Django 2.2 on 2021-01-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images', verbose_name='Изображение'),
        ),
    ]
