# Generated by Django 2.2 on 2019-04-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0014_auto_20190420_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
