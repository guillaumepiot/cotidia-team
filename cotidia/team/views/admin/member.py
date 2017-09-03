import django_filters

from django.db.models import Q

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


class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Name",
        method="filter_name"
    )

    class Meta:
        model = Member
        fields = ['name', 'active']

    def filter_name(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
        )


class MemberList(AdminListView):
    columns = (
        ('Name', 'name'),
        ('Role', 'role'),
        ('Slug', 'slug'),
        ('Active', 'active'),
    )
    model = Member
    filterset = MemberFilter
    template_type = "centered"


class MemberDetail(AdminDetailView):
    model = Member
    fieldsets = [
        {
            "legend": "Member details",
            "fields": [
                [
                    {
                        "label": "Name",
                        "field": "name",
                    }
                ],
                {
                    "label": "Role",
                    "field": "role",
                },
                {
                    "label": "Slug",
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
        {
            "legend": "Social networks",
            "template_name": "admin/team/member/social_networks.html"
        }
    ]


class MemberCreate(AdminCreateView):
    model = Member
    form_class = MemberAddForm


class MemberUpdate(AdminUpdateView):
    model = Member
    form_class = MemberUpdateForm


class MemberDelete(AdminDeleteView):
    model = Member
