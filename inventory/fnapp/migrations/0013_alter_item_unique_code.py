# Generated by Django 4.0.4 on 2022-06-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0012_alter_item_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unique_code',
            field=models.IntegerField(default=79252536, editable=False),
        ),
    ]
