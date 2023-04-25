# shortcuts
from django.shortcuts import redirect, render, get_object_or_404

# tables
from .models import Member

# forms
from django.forms import modelform_factory
# from .forms import MemberFrom

# caching stuff
from django.views.decorators.cache import cache_page

#pagination
from django.core.paginator import Paginator


# Memebers
MemberForm = modelform_factory(Member, exclude=["role"]) # role is excluded as
# it is set using default.

@cache_page(1) # test caching - would change when out of production.
def memberCreate(request):
    if request.method == "POST": # if the user submits the form
        form = MemberForm(request.POST) # to prevent user having to reenter data
        if form.is_valid():             # incase of failed submit.
            form.save()
            return redirect("home")
    else:
        form = MemberForm()
    return render(request, "member/member-create.html", {"form": form})

def memberDetail(request, id): # will have update and delete buttons
    member = get_object_or_404(Member, pk=id)
    return render(request, "member/member-detail.html", {"member": member})

# couldnt work out how to just pass member rather then just the id
def memberUpdate(request, id):
    member = get_object_or_404(Member, pk=id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "member/member-update.html", {"member": member, 
                                                        "form": form})

def memberDelete(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == "POST":
        member.delete()
        return redirect("home")
    return render(request, "member/member-delete.html", {"member": member})