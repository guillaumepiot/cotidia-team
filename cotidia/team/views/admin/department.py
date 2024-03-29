import django_filters

from django.urls import reverse
from django.contrib import messages
from django import forms

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminDeleteView,
    AdminCreateView,
    AdminUpdateView,
)
from cotidia.team.models import Department
from cotidia.team.forms.admin.department import DepartmentAddForm, DepartmentUpdateForm


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Name",
        method="filter_name",
        widget=forms.TextInput(attrs={"placeholder": "Search"}),
    )

    class Meta:
        model = Department
        fields = ["name"]


class DepartmentList(AdminListView):
    columns = (("ID", "id"), ("Order", "order"), ("name", "name"))
    model = Department
    template_type = "centered"
    filterset = DepartmentFilter


class DepartmentDetail(AdminDetailView):
    model = Department
    permission_required = "team.change_model"
    fieldsets = [
        {
            "legend": "Department Details",
            "fields": [
                [
                    {"label": "ID", "field": "id"},
                    {"label": "order id", "field": "order_id"},
                    {"label": "name", "field": "name"},
                ]
            ],
        }
    ]


class DepartmentCreate(AdminCreateView):
    model = Department
    form_class = DepartmentAddForm
    permission_required = "team.add_model"

    def get_success_url(self):
        messages.success(self.request, "Department has been created.")
        return reverse("team-admin:department-detail", kwargs={"pk": self.object.id})


class DepartmentUpdate(AdminUpdateView):
    model = Department
    form_class = DepartmentUpdateForm
    permission_required = "team.change_model"
    fieldsets = [
        {
            "legend": "Department Details",
            "fields": [
                [
                    {"label": "ID", "field": "id"},
                    {"label": "order id", "field": "order_id"},
                    {"label": "name", "field": "name"},
                ]
            ],
        }
    ]

    def get_success_url(self):
        messages.success(self.request, "Department details have been updated.")
        return reverse("team-admin:department-detail", kwargs={"pk": self.object.id})


class DepartmentDelete(AdminDeleteView):
    model = Department
    permission_required = "app.delete_model"

    def get_success_url(self):
        messages.success(self.request, "Department has been deleted.")
        return reverse("team-admin:department-list")
