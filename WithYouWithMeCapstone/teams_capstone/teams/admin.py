from django.contrib import admin
from .models import Member, Team, Location, Manager
# Register your models here.

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Location)
admin.site.register(Manager)
