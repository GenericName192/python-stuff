from django.urls import path
from views import managerCreate, managerDetails, managerUpdate, managerPage

urlpatterns = [
    path("manager", managerPage, name="managerPage"),
    path("create-manager", managerCreate, name="managerCreate"),
    path("manager-detail/<int:id>", managerDetails, name="managerDetails"),
    path("manager-update/<int:id>", managerUpdate, name="managerUpdate")
]