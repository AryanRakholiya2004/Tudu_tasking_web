# Generated by Django 5.0.2 on 2024-06-24 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
        ('tudu_app', '0006_task_type_lists_google_user_tasks_data_google_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks_data',
            name='added_by_google',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
    ]
