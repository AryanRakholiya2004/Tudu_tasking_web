# Generated by Django 5.0.2 on 2024-06-22 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task_type_lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=100)),
                ('task_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=100)),
                ('user_loged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tasks_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=250)),
                ('task_desc', models.TextField()),
                ('task_modified', models.DateTimeField(auto_now_add=True)),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tudu_app.task_type_lists')),
            ],
        ),
        migrations.AddField(
            model_name='task_type_lists',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tudu_app.user_data'),
        ),
    ]
