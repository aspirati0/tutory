# Generated by Django 4.1.5 on 2023-02-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
