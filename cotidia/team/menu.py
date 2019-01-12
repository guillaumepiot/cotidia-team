from django.urls import reverse


def admin_menu(context):
    return [
        {
            "icon": "users",
            "text": "Team management",
            "description": "Manage members and departments.",
            "align_right": True,
            "nav_items": [
                {
                    "text": "Members",
                    "icon": "users",
                    "url": reverse("team-admin:member-list"),
                    "permissions": ["team.add_member", "team.change_member"],
                },
                {
                    "text": "Departments",
                    "icon": "building",
                    "url": reverse("team-admin:department-list"),
                    "permissions": ["team.add_department", "team.change_department"],
                },
            ],
        }
    ]
