from django.contrib import admin
from apps.models import Blogger


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
