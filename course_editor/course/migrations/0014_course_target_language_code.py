# Generated by Django 3.0.1 on 2020-01-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20200103_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='target_language_code',
            field=models.TextField(default='', verbose_name='Target langauge IETF BCP 47 code'),
            preserve_default=False,
        ),
    ]
