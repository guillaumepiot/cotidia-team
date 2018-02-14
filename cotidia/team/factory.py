import factory


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'team.department'
