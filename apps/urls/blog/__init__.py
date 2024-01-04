from django.urls import include, path
from .blogs import urlpatterns as blogs_urlpatterns

urlpatterns = (
    [
        path("blogs/", include(blogs_urlpatterns)),
    ],
    "blog",
)
