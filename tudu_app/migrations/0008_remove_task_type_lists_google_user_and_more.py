# Generated by Django 5.0.2 on 2024-06-24 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
        ('tudu_app', '0007_tasks_data_added_by_google'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_type_lists',
            name='google_user',
        ),
        migrations.RemoveField(
            model_name='tasks_data',
            name='google_user',
        ),
        migrations.AddField(
            model_name='task_type_lists',
            name='added_by_google',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
        migrations.AlterField(
            model_name='task_type_lists',
            name='added_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tudu_app.user_data'),
        ),
    ]
