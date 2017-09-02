from django.conf.urls import url

from cotidia.team.views.admin.member import (
    MemberList,
    MemberCreate,
    MemberDetail,
    MemberUpdate,
    MemberDelete
)

urlpatterns = [
    url(
        r'^members/$',
        MemberList.as_view(),
        name='member-list'
    ),
    url(
        r'^member/add$',
        MemberCreate.as_view(),
        name='member-add'
    ),
    url(
        r'^member/(?P<pk>[\d]+)$',
        MemberDetail.as_view(),
        name='member-detail'
    ),
    url(
        r'^member/(?P<pk>[\d]+)/update$',
        MemberUpdate.as_view(),
        name='member-update'
    ),
    url(
        r'^member/(?P<pk>[\d]+)/delete$',
        MemberDelete.as_view(),
        name='member-delete'
    ),
]
