# Generated by Django 5.0.2 on 2024-06-24 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tudu_app', '0004_delete_tasks_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=250)),
                ('task_desc', models.TextField()),
                ('task_modified', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tudu_app.user_data')),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tudu_app.task_type_lists')),
            ],
        ),
    ]
