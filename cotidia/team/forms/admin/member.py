from django import forms
from betterforms.forms import BetterModelForm

from cotidia.team.models import Member
from cotidia.admin.widgets import TrixEditor


class MemberAddForm(BetterModelForm):

    bio = forms.CharField(widget=TrixEditor, required=False)

    class Meta:
        model = Member
        exclude = ['created_at', 'updated_at', 'order_id']
        fieldsets = (
            ('info', {
                'fields': (
                    ('first_name', 'last_name'),
                    'slug',
                    'role',
                    'department',
                    'bio',
                    ('email', 'phone'),
                    'active',
                ),
                'legend': 'Member details'
            }),
            ('photo', {
                'fields': (
                    'photo',
                ),
                'legend': 'Photo'
            }),
        )


class MemberUpdateForm(MemberAddForm):
    class Meta:
        model = Member
        exclude = ['created_at', 'updated_at', 'order_id']
