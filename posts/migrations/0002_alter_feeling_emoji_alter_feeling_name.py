# Generated by Django 5.0.1 on 2024-10-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeling',
            name='emoji',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='feeling',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
