from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(blank=True, default='')
    phone_number = models.IntegerField(default=0)
    company = models.CharField(max_length=50, default='')


class Property(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(default=0)
    size_length = models.IntegerField(default=0, blank=True)
    size_width = models.IntegerField(default=0, blank=True)
    size_total = models.IntegerField(default=0, blank=True)
    # agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Feature(models.Model):
    feature = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.feature
