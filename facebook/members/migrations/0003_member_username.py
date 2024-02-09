# Generated by Django 5.0.1 on 2024-02-09 16:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
