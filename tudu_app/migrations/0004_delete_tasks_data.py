# Generated by Django 5.0.2 on 2024-06-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tudu_app', '0003_alter_tasks_data_added_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tasks_data',
        ),
    ]
