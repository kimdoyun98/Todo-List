# Generated by Django 4.0.3 on 2022-03-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sign', '0002_user_info_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]