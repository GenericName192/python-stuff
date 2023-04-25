# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Team
from member.models import Member


# forms
from django.forms import modelform_factory
# from .forms import MemberFrom

# caching stuff
from django.views.decorators.cache import cache_page

#pagination
from django.core.paginator import Paginator
# Create your views here.
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
    return render(request, "team/team-create.html", {"form": form})

def teamDetail(request, id): # will have update and delete
    team = get_object_or_404(Team, pk=id)
    members = Member.objects.filter(team_id = id)
    if request.method == "POST":
        team.delete()
        return redirect("home")
    return render(request, "team/team-detail.html", {"team": team,
                                                      "members": members})

def teamUpdate(request, id):
    team = get_object_or_404(Team, pk=id)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "team/team-update.html", {"team": team, 
                                                    "form": form})

def teamDelete(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        team.delete()
        return redirect("home")
    return render(request, "team/team-delete.html", {"team": team})