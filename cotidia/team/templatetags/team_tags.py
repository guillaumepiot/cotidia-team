from django import template

from cotidia.team.models import Member, Department

register = template.Library()


@register.simple_tag
def get_departments():
    return Department.objects.all().order_by('order_id')

@register.simple_tag
def get_team_members():
    return Member.objects.filter(active=True).order_by('order_id')
