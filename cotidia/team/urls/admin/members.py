from django.conf.urls import url, include

from cotidia.team.views.admin.member import (
    MemberList,
    MemberCreate,
    MemberDetail,
    MemberUpdate,
    MemberDelete,
)
from cotidia.team.views.admin.department import (
    DepartmentList,
    DepartmentCreate,
    DepartmentDetail,
    DepartmentUpdate,
    DepartmentDelete,
)
from cotidia.team.views.admin.membersocial import (
    MemberSocialCreate,
    MemberSocialUpdate,
    MemberSocialDelete
)

urlpatterns = [
    url(
        r'^$',
        MemberList.as_view(),
        name='member-list'
    ),
    url(
        r'^add$',
        MemberCreate.as_view(),
        name='member-add'
    ),
    url(
        r'^(?P<pk>[\d]+)$',
        MemberDetail.as_view(),
        name='member-detail'
    ),
    url(
        r'^(?P<pk>[\d]+)/update$',
        MemberUpdate.as_view(),
        name='member-update'
    ),
    url(
        r'^(?P<pk>[\d]+)/delete$',
        MemberDelete.as_view(),
        name='member-delete'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/add$',
        MemberSocialCreate.as_view(),
        name='membersocial-add'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/(?P<pk>[\d]+)/update$',
        MemberSocialUpdate.as_view(),
        name='membersocial-update'
    ),
    url(
        r'^(?P<parent_id>[\d]+)/social/(?P<pk>[\d]+)/delete$',
        MemberSocialDelete.as_view(),
        name='membersocial-delete'
    ),
]
