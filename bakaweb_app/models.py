from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    url = models.URLField(null=False)
    user_name = models.CharField(max_length=512)
    pw = models.CharField(max_length=512)
    first_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name