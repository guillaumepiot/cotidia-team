import factory
import factory.fuzzy

from faker import Faker
from faker.providers import profile, company

from cotidia.team.models import Department


fake = Faker("en_GB")
fake.add_provider(profile)
fake.add_provider(company)


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "team.department"

    name = factory.LazyFunction(lambda: fake.company())


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "team.member"

    first_name = factory.Faker("first_name", locale="en_GB")
    last_name = factory.Faker("last_name", locale="en_GB")
    role = factory.LazyFunction(lambda: fake.job())
    bio = factory.LazyFunction(lambda: fake.paragraphs(nb=2, ext_word_list=None))
    email = factory.Faker("email", locale="en_GB")
    phone = factory.LazyFunction(lambda: fake.phone_number())

    active = True
    department = factory.LazyFunction(
        lambda: Department.objects.all().order_by("?").first()
    )
