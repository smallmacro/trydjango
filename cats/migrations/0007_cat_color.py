# Generated by Django 3.1.2 on 2021-08-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_auto_20210820_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('OG', 'Orange'), ('WH', 'white'), ('BK', 'black')], default='WH', max_length=2),
        ),
    ]