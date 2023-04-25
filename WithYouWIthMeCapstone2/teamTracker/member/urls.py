from django.urls import path
from member.views import memberCreate,memberDetail,memberUpdate,memberDelete

urlpatterns = [
    path("create", memberCreate, name="memberCreate"),
    path("detail/<int:id>", memberDetail, name="memberDetail"),
    path("update/<int:id>", memberUpdate, name="memberUpdate"),
    path("delete/<int:id>", memberDelete, name="memberDelete"),
    ]