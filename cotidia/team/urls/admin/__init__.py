from django.urls import re_path, include

app_name = "team"
urlpatterns = [
    re_path(r'^member/',
            include("cotidia.team.urls.admin.members")),
    re_path(r'^department/',
            include("cotidia.team.urls.admin.department"))
    ]
