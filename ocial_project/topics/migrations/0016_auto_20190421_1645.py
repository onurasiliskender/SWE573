# Generated by Django 2.2 on 2019-04-21 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0015_section_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Section')),
            ],
        ),
    ]
