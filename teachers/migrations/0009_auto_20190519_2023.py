# Generated by Django 2.1.5 on 2019-05-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_auto_20190430_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='desig',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_principal',
            field=models.BooleanField(default=False),
        ),
    ]
