from datetime import date
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default="member")
    startDate = models.DateField(default = date.today())
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default="manager")
    startDate = models.DateField(default = date.today())
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
