# Generated by Django 4.0.5 on 2022-06-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', 'HIGH'), ('2', 'MEDIUM'), ('3', 'LOW')], default='UI', max_length=3),
        ),
    ]
