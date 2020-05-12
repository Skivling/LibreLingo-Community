# Generated by Django 3.0.5 on 2020-05-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0040_auto_20200518_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativeSolutionInTargetLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField(verbose_name='Alternative solution')),
                ('sentence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.LearnSentence')),
                ('word', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.LearnWord')),
            ],
            options={
                'verbose_name': 'Alternative solution in target language',
                'verbose_name_plural': 'Alternative solutions in target language',
                'unique_together': {('sentence', 'word', 'solution')},
            },
        ),
    ]
