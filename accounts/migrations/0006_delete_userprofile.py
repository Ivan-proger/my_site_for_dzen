# Generated by Django 3.1.5 on 2021-02-09 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210209_1807'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
