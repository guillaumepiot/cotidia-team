from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminCreateView,
    AdminUpdateView,
    AdminDeleteView,
)

from cotidia.team.models import Member
from cotidia.team.forms.admin.member import (
    MemberAddForm,
    MemberUpdateForm,
)


class MemberList(AdminListView):
    columns = (
        ('Name', 'name'),
        ('Role', 'role'),
        ('Active', 'active'),
    )
    model = Member


class MemberDetail(AdminDetailView):
    model = Member
    fieldsets = [
        {
            "legend": "Member details",
            "fields": [
                # [
                #     {
                #         "label": "Name",
                #         "field": "name",
                #     }
                # ],
                {
                    "label": "Role",
                    "field": "role",
                },
                {
                    "label": "URL",
                    "field": "slug",
                },
                {
                    "label": "Biography",
                    "field": "bio",
                },
                [
                    {
                        "label": "Email",
                        "field": "email",
                    },
                    {
                        "label": "Phone",
                        "field": "phone",
                    }
                ],
                {
                    "label": "Active",
                    "field": "active",
                },
            ]
        },
        {
            "legend": "Photo",
            "fields": [
                {
                    "label": "Photo",
                    "field": "photo",
                }
            ]
        },
        # {
        #     "legend": "Social networks",
        #     "template_name": "admin/team/member/social_networks.html"
        # }
    ]


class MemberCreate(AdminCreateView):
    model = Member
    form_class = MemberAddForm


class MemberUpdate(AdminUpdateView):
    model = Member
    form_class = MemberUpdateForm


class MemberDelete(AdminDeleteView):
    model = Member
