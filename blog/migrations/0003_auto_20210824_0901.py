# Generated by Django 3.1.2 on 2021-08-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210824_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]