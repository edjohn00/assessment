from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin
from typing import Sequence

class TemplateLocationMixin(TemplateResponseMixin):
    template_location = None

    def get_namespace(self) -> str:
        return resolve(self.request.path).namespace

    def get_template_location(self) -> str:
        namespace = self.get_namespace()
        return namespace.replace(":", "/")

    def get_template_names(self) -> Sequence[str]:
        return [self.get_template()]

    def get_base_location(self) -> str:
        namespace = self.get_namespace()
        return "/".join(namespace.split(":")[0:2])

    def get_template(self) -> str:
        if self.template_location:
            print("Found template 1")
            print(f"{ self.template_location}/{self.template_name}")
            return f"{ self.template_location}/{self.template_name}"
        else:
            print("No Template found 2")
            print(f"{ self.get_template_location()}/{self.template_name}")
            return f"{ self.get_template_location()}/{self.template_name}"