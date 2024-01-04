from django.urls import path
from apps.views.blogs import blogs

urlpatterns = (
    [
        path("", blogs.IndexView.as_view(), name="index"),
    ],
    "blogs",
)
