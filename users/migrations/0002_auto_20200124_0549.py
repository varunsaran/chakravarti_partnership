# Generated by Django 3.0.1 on 2020-01-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sheets_id',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]