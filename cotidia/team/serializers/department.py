from cotidia.admin.serializers import BaseDynamicListSerializer

from cotidia.team.models import Department


class DepartmentAdminSerializer(BaseDynamicListSerializer):
    class Meta:
        model = Department
        exclude = ["id"]

    class SearchProvider:
        display_field = "name"
        filters = "__all__"
