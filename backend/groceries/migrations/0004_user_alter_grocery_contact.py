# Generated by Django 4.1.5 on 2023-01-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0003_grocery_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20, null=True)),
                ('profile_pic', models.ImageField(upload_to='profiles/')),
            ],
        ),
        migrations.AlterField(
            model_name='grocery',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groceries.user'),
        ),
    ]
