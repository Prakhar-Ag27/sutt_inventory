# Generated by Django 4.0.4 on 2022-05-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='no_of_issued_items',
            new_name='no_of_items_issued_out',
        ),
        migrations.AlterField(
            model_name='items',
            name='last_issued',
            field=models.DateTimeField(),
        ),
    ]