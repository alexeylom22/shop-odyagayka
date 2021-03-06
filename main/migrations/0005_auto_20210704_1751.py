# Generated by Django 3.2.4 on 2021-07-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_items_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Ціна'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ціна'),
        ),
    ]
