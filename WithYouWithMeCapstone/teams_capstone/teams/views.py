# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Member, Team, Location, Manager

# forms
from django.forms import modelform_factory
# from .forms import MemberFrom

# caching stuff
from django.views.decorators.cache import cache_page

#pagination
from django.core.paginator import Paginator


# Homepage
def homepage(request):
    pMembers = Paginator(Member.objects.all(), 5)
    pTeams = Paginator(Team.objects.all(), 5)
    Mpage = request.GET.get("mPage")
    Tpage = request.GET.get("tPage")
    members = pMembers.get_page(Mpage)
    teams = pTeams.get_page(Tpage)

    return render(request, "teams/homepage.html", {
        "members": members,
        "teams": teams
    })

# Memebers
MemberForm = modelform_factory(Member, exclude=["role"]) # role is excluded as
# it is set using default.

@cache_page(1) # Wanted to see if it would work but annoying during developement, reminder to change later.
def memberCreate(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MemberForm()
    return render(request, "teams/member-create.html", {"form": form})

def memberDetail(request, id): # will have update and delete buttons
    member = get_object_or_404(Member, pk=id)
    return render(request, "teams/member-detail.html", {"member": member})

# couldnt work out how to just pass member rather then just the id
def memberUpdate(request, id):
    member = get_object_or_404(Member, pk=id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "teams/member-update.html", {"member": member, 
                                                        "form": form})

def memberDelete(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == "POST":
        member.delete()
        return redirect("home")
    return render(request, "teams/member-delete.html", {"member": member})
    
TeamForm = modelform_factory(Team, exclude=[])

@cache_page(1) # Wanted to see if it would work but annoying during developement, reminder to change later.
def teamCreate(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeamForm()
    return render(request, "teams/team-create.html", {"form": form})

def teamDetail(request, id): # will have update and delete
    team = get_object_or_404(Team, pk=id)
    members = Member.objects.filter(team_id = id)
    if request.method == "POST":
        team.delete()
        return redirect("home")
    return render(request, "teams/team-detail.html", {"team": team,
                                                      "members": members})

def teamUpdate(request, id):
    team = get_object_or_404(Team, pk=id)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "teams/member-update.html", {"team": team, 
                                                        "form": form})

def teamDelete(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        team.delete()
        return redirect("home")
    return render(request, "teams/team-delete.html", {"team": team})

def locations(request): # view all locations (may have to have this twice)
    p = Paginator(Location.objects.all(), 5)
    page = request.GET.get("page")
    locations = p.get_page(page)
    return render(request, "teams/locations.html", {"locations": locations})

# Manager

def managerPage(request):
    return render(request, "teams/manager-page.html", {
        "members": Member.objects.all(),
        "managers": Manager.objects.all(),
        "teams": Team.objects.all(),
        "locations": Location.objects.all()   
    })

LocationForm = modelform_factory(Location, exclude=[])

def locationCreate(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("managerPage")
    else:
        form = LocationForm()
    return render(request, "teams/location-create.html", {"form": form})

def locationDetail(request, id): # select_related might be better here.
    location = get_object_or_404(Location, pk=id)
    teams = Team.objects.filter(location_id = id)
    return render(request, "teams/location-detail.html", {"location": location,
                                                          "teams": teams})

ManagerForm = modelform_factory(Manager, exclude=["role"])

def managerCreate(request): # User being both Manager
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("managerPage")
    else:
        form = ManagerForm()
    return render(request, "teams/manager-create.html", {"form": form})
    
def managerDetails(request, id):
    manager = get_object_or_404(Manager, pk=id)
    if request.method == "POST":
        manager.delete()
        return redirect("home")
    return render(request, "teams/manager-detail.html", {"manager": manager})

def managerUpdate(request, id):
    manager = get_object_or_404(Manager, pk=id)
    form = ManagerForm(request.POST or None, instance=manager)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "teams/member-update.html", {"manager": manager, 
                                                        "form": form})
