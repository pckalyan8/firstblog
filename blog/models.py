from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import AccountUser
from djtwo import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(AccountUser,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
