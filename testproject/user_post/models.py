from django.conf import settings
from django.db import models


class Postsjson(models.Model):
    userId = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.body


class Usersjson(models.Model):
    user_id = models.ForeignKey(Postsjson, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.JSONField()

    def __str__(self):
        return self.name


class UsersPosts(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.JSONField()
    body = models.TextField()

    def __str__(self):
        return self.name
