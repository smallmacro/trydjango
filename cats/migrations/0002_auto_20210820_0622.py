# Generated by Django 3.1.2 on 2021-08-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(null=True),
        ),
    ]