from django.db import models
from datetime import date
from team.models import Team, Location
# from location.models import Location

class Manager(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default="manager")
    startDate = models.DateField(default = date.today())
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name