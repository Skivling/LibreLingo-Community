# Generated by Django 3.0.1 on 2020-01-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20200103_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='source_language_name',
            field=models.TextField(default='English', verbose_name='Source langauge name'),
            preserve_default=False,
        ),
    ]
