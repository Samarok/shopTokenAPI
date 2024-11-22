from django.db import models
from uuid import uuid4


class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

class Token(models.Model):
    token = models.CharField(max_length=36, unique=True, default=uuid4())

    def __str__(self):
        return str(self.token)