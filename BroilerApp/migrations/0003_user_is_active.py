# Generated by Django 5.0.4 on 2024-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BroilerApp', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
