# Generated by Django 4.2.1 on 2023-05-12 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_rename_author_ad_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
    ]