# Generated by Django 4.0.2 on 2022-02-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('usado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('activida', models.CharField(max_length=100)),
            ],
        ),
    ]