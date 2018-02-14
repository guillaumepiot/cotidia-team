from django import forms

from betterforms.forms import BetterModelForm

from cotidia.team.models import Department


class DepartmentAddForm(BetterModelForm):

    class Meta:
        model = Department
        fields = [
            "name",
        ]
        fieldsets = (
            ('info', {
                'fields': (
                    'name',
                ),
                'legend': 'Department details'
            }),
        )


class DepartmentUpdateForm(BetterModelForm):

    class Meta:
        model = Department
        fields = [
            "name",
        ]
        fieldsets = (
            ('info', {
                'fields': (
                    'name',
                ),
                'legend': 'Department details'
            }),
        )
