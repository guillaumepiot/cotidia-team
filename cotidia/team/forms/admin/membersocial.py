from betterforms.forms import BetterModelForm

from cotidia.team.models import MemberSocial


class MemberSocialAddForm(BetterModelForm):
    class Meta:
        model = MemberSocial
        exclude = ['created_at', 'updated_at', 'member']
        fieldsets = (
            ('info', {
                'fields': (
                    ('network', 'url',),
                ),
                'legend': 'Member social network'
            }),
        )


class MemberSocialUpdateForm(BetterModelForm):
    class Meta:
        model = MemberSocial
        exclude = ['created_at', 'updated_at', 'member']
        fieldsets = (
            ('info', {
                'fields': (
                    ('network', 'url',),
                ),
                'legend': 'Member social network'
            }),
        )
