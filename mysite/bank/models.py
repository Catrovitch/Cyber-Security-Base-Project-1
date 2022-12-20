import datetime

from django.db import models
from django.utils import timezone


class Account(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    admin = models.BooleanField(default=False)
    #fix for FLAW 1 
    #remove admin field
    #add specific role filed???
    def __str__(self):
        return str(self.username)

class Creditcard(models.Model):
    number = models.CharField(max_length=26)
    credit = models.IntegerField(number)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.pk)