# Generated by Django 3.0.5 on 2022-04-03 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0013_auto_20220403_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 18, 30, 25, 484156)),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 18, 30, 25, 484435)),
        ),
    ]
