# Generated by Django 3.1.5 on 2021-02-08 11:38

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='заголовок статьи'),
            preserve_default=False,
        ),
    ]
