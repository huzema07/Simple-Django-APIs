# Generated by Django 5.0.6 on 2024-05-19 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaAPI', '0002_alter_pizza_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
