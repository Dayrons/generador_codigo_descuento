# Generated by Django 4.0.2 on 2022-02-15 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='activida',
            new_name='capital',
        ),
    ]
