# Generated by Django 2.1.1 on 2018-09-23 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20180906_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='is_varified',
            new_name='is_verified',
        ),
    ]
