from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from typing import Any, Sequence
from django_htmx.http import trigger_client_event
from django.shortcuts import render


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


class HtmxResponseMixin(TemplateLocationMixin, ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context["base_template"] = f"{self.get_base_location()}/partial.html"
        else:
            context["base_template"] = f"{self.get_base_location()}/base.html"
        return context


class ModalMixin:
    modal_template = "blog/common/modal.html"
    modal_title = None
    modal_messgae = None
    modal_form_action = None
    modal_show = "modal-show"
    modal_hx_swap = None
    modal_allowed_close = True
    modal_allowed_delete = False
    modal_submit_class = "btn btn-primary"
    modal_submit_value = "Submit"
    modal_hx_boost = True
    modal_hx_push_url = False

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        response = render(request, self.modal_template, context)
        return trigger_client_event(response, self.modal_show)
