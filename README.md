# Cotidia team

A plugin to manage team members on a team page. This is primarily used for a brochure
site to display a list of people within a team.

```console
$ pip install -e git+git@code.cotidia.com:cotidia/team.git#egg=cotidia-team
```

## Settings

Add `cotidia.team` to your INSTALLED_APPS:

```python
INSTALLED_APPS=[
    ...
    "cotidia.team",

]
```

## Template tags

In order to retrieve all the team members on a page, you can use the
template tag `get_team_members`.

It will return all the active members in order of order id.

```html
{% load team_tags %}
{% get_team_members as members %}

{% for member in members %}
    {{member}}
{% endfor %}
```
