# Generated by Django 4.0.4 on 2022-06-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0007_item_student_through_delete_issue_items_delete_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unique_code',
            field=models.IntegerField(default=83263174, editable=False),
        ),
        migrations.AlterField(
            model_name='through',
            name='time_of_issue',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='through',
            name='time_of_return',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
