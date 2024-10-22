# Generated by Django 5.0.6 on 2024-06-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondatab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zzmessages',
            name='message',
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
