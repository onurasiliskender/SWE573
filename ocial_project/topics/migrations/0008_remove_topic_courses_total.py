# Generated by Django 2.2 on 2019-04-14 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_auto_20190414_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='courses_total',
        ),
    ]
