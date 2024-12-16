# task1/models.py
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.IntegerField()
    registration_date = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.age < 0:
            raise ValidationError("Возраст не может быть отрицательным")
        if self.balance < 0:
            raise ValidationError("Баланс не может быть отрицательным")

    def __str__(self):
        return f"{self.name} (Баланс: {self.balance})"

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title