# Generated by Django 4.0.3 on 2022-03-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('user_pw', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
