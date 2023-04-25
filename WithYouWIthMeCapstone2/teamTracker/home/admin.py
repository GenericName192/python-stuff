from django.contrib import admin
from member.models import Member,Team,Location
from manager.models import Manager

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Location)
admin.site.register(Manager)
