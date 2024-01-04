from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from apps.views.mixin import HtmxResponseMixin
from apps.models import Blog


class IndexView(LoginRequiredMixin, HtmxResponseMixin, generic.ListView):
    template_name = "index.html"
    model = Blog
    paginate_by = 5
