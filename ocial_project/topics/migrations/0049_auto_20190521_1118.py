# Generated by Django 2.2 on 2019-05-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0048_auto_20190521_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='completeRate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='quiz',
            name='completeRate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
