# Generated by Django 4.0.3 on 2022-03-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_todo',
            name='context',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main_todo',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
