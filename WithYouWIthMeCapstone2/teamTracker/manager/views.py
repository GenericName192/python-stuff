# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Manager
from member.models import Member, Team, Location

# forms
from django.forms import modelform_factory
# from .forms import MemberFrom

# caching stuff
from django.views.decorators.cache import cache_page

#pagination
from django.core.paginator import Paginator

# Manager

ManagerForm = modelform_factory(Manager, exclude=["role"])

def managerPage(request):
    return render(request, "teams/manager-page.html", {
        "members": Member.objects.all(),
        "managers": Manager.objects.all(),
        "teams": Team.objects.all(),
        "locations": Location.objects.all()   
    })

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