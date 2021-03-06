# Generated by Django 4.0.3 on 2022-03-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='guest', max_length=20)),
                ('context', models.TextField(null=None)),
                ('is_complete', models.BooleanField(default=False)),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'main_todolist',
            },
        ),
    ]
