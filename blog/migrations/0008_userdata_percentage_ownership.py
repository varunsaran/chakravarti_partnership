# Generated by Django 3.0.1 on 2020-01-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='percentage_ownership',
            field=models.FloatField(default=0.0),
        ),
    ]
