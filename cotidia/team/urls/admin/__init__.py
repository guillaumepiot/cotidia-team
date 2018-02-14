from django.urls import path, include

app_name = "team"
urlpatterns = [
    path('member/',
            include("cotidia.team.urls.admin.members")),
    path('department/',
            include("cotidia.team.urls.admin.department"))
    ]
