# Generated by Django 2.2 on 2019-05-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0043_auto_20190521_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner_course_record',
            name='completeRate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='learner_section_record',
            name='completeRate',
            field=models.FloatField(default=0),
        ),
    ]