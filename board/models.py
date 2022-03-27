from django.db import models


class Main_Todo(models.Model):
    user_id = models.CharField(max_length=20, null=False, default='guest')
    context = models.TextField(null=False)
    is_complete = models.BooleanField(default=False)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'main_todolist'


class Day_Todo(models.Model):
    user_id = models.CharField(max_length=20, null=False, default='guest')
    context = models.TextField(null=False)
    is_complete = models.BooleanField(default=False)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'day_todolist'


class Sub_Todo(models.Model):
    user_id = models.CharField(max_length=20, null=False, default='guest')
    context = models.TextField(null=False)
    is_complete = models.BooleanField(default=False)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = 'sub_todolist'