"""
URL configuration for teams_capstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.urls import include, path
from teams.views import homepage, memberDetail, teamDetail, memberCreate, \
                        teamCreate, locations, locationCreate, managerPage, \
                        locationDetail, managerCreate, managerDetails, \
                        memberUpdate, teamUpdate, managerUpdate, memberDelete, \
                        teamDelete

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", homepage, name="home"),
    path("member-create", memberCreate, name="memberCreate"),
    path("member-detail/<int:id>", memberDetail, name="memberDetail"),
    path("member-update/<int:id>", memberUpdate, name="memberUpdate"),
    path("member-delete/<int:id>", memberDelete, name="memberDelete"),
    path("team-create", teamCreate, name="teamCreate"),
    path("team-detail/<int:id>", teamDetail, name="teamDetail"),
    path("team-update/<int:id>", teamUpdate, name="teamUpdate"),
    path("team-delete/<int:id>", teamDelete, name="teamDelete"),
    path("locations", locations, name="locations"),
    path("location-detail/<int:id>", locationDetail, name="locationDetail"),
    path('__debug__/', include('debug_toolbar.urls')),
    # Admin pages
    # path("manager", managerPage, name="managerPage"),
    # path("create-location", locationCreate, name="locationCreate"),
    # path("create-manager", managerCreate, name="managerCreate"),
    # path("manager-detail/<int:id>", managerDetails, name="managerDetails"),
    # path("manager-update/<int:id>", managerUpdate, name="managerUpdate")
]
