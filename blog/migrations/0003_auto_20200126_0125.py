# Generated by Django 3.0.1 on 2020-01-26 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='sheets_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
