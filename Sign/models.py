from django.db import models


class User_Info(models.Model):
    user_id = models.CharField(max_length=20, unique=True, null=False)
    user_pw = models.CharField(max_length=256, null=False)
    username = models.CharField(max_length=20, null=False)
    is_active = models.BooleanField(null=True, default=False)
