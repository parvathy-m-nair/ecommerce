# Generated by Django 4.1.5 on 2023-02-07 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ceated',
            new_name='created',
        ),
    ]
