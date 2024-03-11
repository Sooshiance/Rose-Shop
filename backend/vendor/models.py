from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Vendor(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    phone  = models.CharField(max_length = 11)
    city  = models.CharField(max_length = 50)
    bio  = models.CharField(max_length = 244)

    def __str__(self):
        return f'{self.user} {self.phone}'    
