#from django.conf import settings
from django.db import models





class Usersjson(models.Model):
#    user = models.ForeignKey(Postsjson.userId, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<User #{self.pk} {self.name!r}>"

class Postsjson(models.Model):
    userId = models.ForeignKey(Usersjson, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body


class UsersPosts(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<User #{self.pk} {self.name!r}>"
