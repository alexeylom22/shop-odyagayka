# Generated by Django 3.2.4 on 2021-07-01 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_items_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
