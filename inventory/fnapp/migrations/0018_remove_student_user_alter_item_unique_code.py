# Generated by Django 4.0.4 on 2022-06-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnapp', '0017_alter_item_unique_code_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='item',
            name='unique_code',
            field=models.IntegerField(default=48088437, editable=False),
        ),
    ]
