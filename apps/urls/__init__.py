from django.urls import include, path
from .account import urlpatterns as account_urlpatterns
from .blog import urlpatterns as blog_urlpatterns

app_name = "apps"

urlpatterns = [
    path("accounts/", include(account_urlpatterns)),
    path("blog/", include(blog_urlpatterns)),
]
