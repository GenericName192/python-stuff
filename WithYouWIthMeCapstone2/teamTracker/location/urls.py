from django.urls import path
from location.views import locations, locationCreate, locationDetail

urlpatterns = [
    path("locations", locations, name="locations"),
    path("location-detail/<int:id>", locationDetail, name="locationDetail"),
    # path("create-location", locationCreate, name="locationCreate"),
]