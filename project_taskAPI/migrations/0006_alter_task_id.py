# Generated by Django 5.0.6 on 2024-05-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_taskAPI', '0005_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
