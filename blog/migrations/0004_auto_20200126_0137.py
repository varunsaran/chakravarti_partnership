# Generated by Django 3.0.1 on 2020-01-26 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200126_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='estimated_annual_incom',
            new_name='estimated_annual_income',
        ),
    ]