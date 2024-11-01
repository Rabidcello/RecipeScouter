from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) ##tells that we dont want to auto populate
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")##links user with their data
    ##deletes all notes if user is deleted
    def __str__(self):
        return self.title
# Create your models here.

class UserItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=235)

    def __str__(self):
        return self.title