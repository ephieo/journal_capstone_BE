# Generated by Django 3.0.5 on 2022-03-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0010_quotes_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='img_link',
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='img_link',
        ),
    ]
