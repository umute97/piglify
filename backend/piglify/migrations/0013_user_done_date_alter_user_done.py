# Generated by Django 4.1.5 on 2023-01-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piglify', '0012_rename_done_date_user_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='done_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
