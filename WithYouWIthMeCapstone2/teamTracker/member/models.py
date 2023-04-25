from datetime import date
from django.db import models
# from location.models import Location
from team.models import Team, Location


class Member(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default="member") # Allows for auto set
    startDate = models.DateField(default = date.today(), verbose_name="Start date")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
