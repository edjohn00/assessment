from django.urls import path
from apps.views.account import profile

urlpatterns = (
    [
        path("", profile.IndexView.as_view(), name="index"),
    ],
    "profile",
)