from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    blogger = models.ForeignKey("apps.Blogger", on_delete=models.CASCADE)
    title = models.CharField(max_lenght=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blog")
        default_verbose_name = "blog"
