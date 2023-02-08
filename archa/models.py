from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    users = models.ManyToManyField(User, through='Permission')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

class Permission(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=[("user", "user"), ("admin", "admin")])

    def __str__(self):
        return self.level + " status for " + self.user.first_name + " " + self.user.last_name + " at " + self.company.name

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    number = models.CharField(max_length=len('1234-1234-1234-1234'))
    expiration = models.DateField()
    limit = models.DecimalField(max_digits=16, decimal_places=2)
    spent = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return "Card for " + self.user.first_name + " " + self.user.last_name + " at " + self.company.name
