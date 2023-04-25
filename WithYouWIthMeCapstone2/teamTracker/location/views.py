# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Location
from team.models import Team

# forms
from django.forms import modelform_factory

#pagination
from django.core.paginator import Paginator

def locations(request): # view all locations (may have to have this twice)
    p = Paginator(Location.objects.all(), 5)
    page = request.GET.get("page")
    locations = p.get_page(page)
    return render(request, "location/locations.html", {"locations": locations})


LocationForm = modelform_factory(Location, exclude=[])

def locationCreate(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("managerPage")
    else:
        form = LocationForm()
    return render(request, "location/location-create.html", {"form": form})

def locationDetail(request, id): # select_related might be better here.
    location = get_object_or_404(Location, pk=id)
    teams = Team.objects.filter(location_id = id)
    return render(request, "location/location-detail.html", {"location": location,
                                                          "teams": teams})