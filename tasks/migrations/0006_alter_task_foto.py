# Generated by Django 4.2.6 on 2023-11-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_campo1_task_campo2_task_campo3_task_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='foto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]