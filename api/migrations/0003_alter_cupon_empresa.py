# Generated by Django 4.0.2 on 2022-02-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_activida_empresa_capital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='empresa',
            field=models.IntegerField(),
        ),
    ]