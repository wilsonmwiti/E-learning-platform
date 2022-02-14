# Generated by Django 4.0.2 on 2022-02-04 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '254712345678. Up to 12 digits allowed.", regex='^(254)([7][0-9]|[1][0-1]){1}[0-9]{1}[0-9]{6}$')]),
        ),
    ]
