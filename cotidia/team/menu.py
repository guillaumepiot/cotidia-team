from django.urls import reverse


def admin_menu(context):
    return [
        {
            "text": "Team",
            "icon": "users",
            "url": reverse("team-admin:member-list"),
            "permissions": ["team.add_member", "team.change_member"],
        }, {
            "text": "department",
            "icon": "warning",
            "url": reverse("team-admin:department-list"),
            "permissions": ["team.add_department",
                            "team.change_department"],
        },
    ]
