from cotidia.admin.views import (
    AdminChildCreateView,
    AdminChildUpdateView,
    AdminChildDeleteView,
)

from cotidia.team.models import MemberSocial
from cotidia.team.forms.admin.membersocial import (
    MemberSocialAddForm,
    MemberSocialUpdateForm,
)
from cotidia.team.models import Member


class MemberSocialCreate(AdminChildCreateView):
    model = MemberSocial
    form_class = MemberSocialAddForm
    parent_model = Member
    parent_model_foreign_key = "member"


class MemberSocialUpdate(AdminChildUpdateView):
    model = MemberSocial
    form_class = MemberSocialUpdateForm
    parent_model = Member
    parent_model_foreign_key = "member"


class MemberSocialDelete(AdminChildDeleteView):
    model = MemberSocial
    parent_model = Member
    parent_model_foreign_key = "member"
