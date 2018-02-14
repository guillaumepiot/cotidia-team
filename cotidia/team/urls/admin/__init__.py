from django.urls import re_path, include

urlpatterns = [
    re_path(r'^member/$',
            include("cotidia.team.urls.admin.members")),
    re_path(r'^department/$',
            include("cotidia.team.urls.admin.department"))
    ]
