# Generated by Django 2.0.1 on 2018-01-25 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20180125_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='updated_at',
            new_name='modified_at',
        )
    ]
