from random import randint

from django.db import models

from faker import Faker
from decimal import Decimal
import datetime
from dateutil.relativedelta import relativedelta

from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=10_000)

    class Meta:
        __tablename__ = 'teachers'

    '''def __repr__(self):
        return f'<Teacher({self.first_name} {self.last_name})>'''

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    '''@classmethod
    def generate_data(cls, count: int):
        faker = Faker()
        for _ in range(count):
            teacher = cls()
            teacher.first_name = faker.first_name()
            teacher.last_name = faker.last_name()
            teacher.birthday = faker.date_between(start_date='-65y', end_date='-25y')
            teacher.salary = Decimal(faker.random_int(min=5000, max=20000))
            teacher.email = f'{teacher.first_name}@test.com'
            teacher.save()
    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years'''

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.salary = randint(10_000, 100_000)
        teacher.save()

