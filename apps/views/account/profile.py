from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from apps.views.mixin import HtmxResponseMixin


class IndexView(LoginRequiredMixin, HtmxResponseMixin, generic.TemplateView):
    template_name = "index.html"
