# Generated by Django 4.1.5 on 2023-01-04 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
