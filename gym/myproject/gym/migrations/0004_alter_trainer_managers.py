# Generated by Django 5.0.7 on 2024-10-09 15:31

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_rename_is_actime_trainer_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='trainer',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
