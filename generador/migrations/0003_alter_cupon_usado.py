# Generated by Django 4.0.2 on 2022-02-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generador', '0002_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='usado',
            field=models.BooleanField(default=False),
        ),
    ]