from django.contrib import admin
from apps.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
