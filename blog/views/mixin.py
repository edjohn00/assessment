from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin
from typing import Sequence


class TemplateLocationMixin(TemplateResponseMixin):
    template_location = None

    def get_namespaces(self) -> str:
        return resolve(self.request.path).namespace

    def get_tempalate_locations(self) -> str:
        return resolve(self.request.path).namespace

    def get_template_locations(self) -> str:
        namespace = self.get_namespaces()
        return namespace.replace(":", "/")

    def get_template_names(self) -> Sequence[str]:
        return [self.get_template()]

    def get_template(self) -> str:
        if self.template_location:
            return f"{self.template_location}/{self.template_name}"
        else:
            return f"{self.get_template_location()}/{self.template_name}"
