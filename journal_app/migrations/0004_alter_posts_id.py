# Generated by Django 4.0.3 on 2022-03-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0003_auto_20220316_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
