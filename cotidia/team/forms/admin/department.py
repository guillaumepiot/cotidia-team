from django import forms

from betterforms.forms import BetterModelForm

from cotidia.team.models import Department


class DepartmentAddForm(BetterModelForm):

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
        ]


class DepartmentUpdateForm(BetterModelForm):

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
        ]
