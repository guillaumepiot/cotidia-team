from rest_framework import serializers

from cotidia.admin.serializers import BaseDynamicListSerializer

from cotidia.team.models import Member
from cotidia.team.serializers.department import DepartmentAdminSerializer


class MemberAdminSerializer(BaseDynamicListSerializer):
    name = serializers.CharField()
    department = DepartmentAdminSerializer()

    class Meta:
        model = Member
        exclude = ["id", "photo"]

    class SearchProvider:
        display_field = "name"
        filters = "__all__"
