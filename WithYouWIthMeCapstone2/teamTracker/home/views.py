# shortcuts
from django.shortcuts import render

# tables
from member.models import Member, Team


#pagination
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
        pMembers = Paginator(Member.objects.all(), 5) # adds pagination to members
        pTeams = Paginator(Team.objects.all(), 5)
        Mpage = request.GET.get("mPage") # 2 pages so they wont affect each other
        Tpage = request.GET.get("tPage")
        members = pMembers.get_page(Mpage)
        teams = pTeams.get_page(Tpage)

        return render(request, "home/homepage.html", {
            "members": members,
            "teams": teams
        })
   
