# Generated by Django 5.0.1 on 2024-10-24 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_feeling_emoji_alter_feeling_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('emoji', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('emoji', models.CharField(max_length=255, unique=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.activity')),
            ],
        ),
    ]
