from betterforms.forms import BetterModelForm

from cotidia.team.models import Member


class MemberAddForm(BetterModelForm):
    class Meta:
        model = Member
        exclude = ['created_at', 'updated_at']
        fieldsets = (
            ('info', {
                'fields': (
                    ('first_name', 'last_name'),
                    'slug',
                    'role',
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


class MemberUpdateForm(BetterModelForm):
    class Meta:
        model = Member
        exclude = ['created_at', 'updated_at']
        fieldsets = (
            ('info', {
                'fields': (
                    ('first_name', 'last_name'),
                    'role',
                    'slug',
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
