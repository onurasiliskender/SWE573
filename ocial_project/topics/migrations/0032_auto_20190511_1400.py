# Generated by Django 2.2 on 2019-05-11 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0031_auto_20190511_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glossary',
            old_name='image',
            new_name='image_url',
        ),
    ]