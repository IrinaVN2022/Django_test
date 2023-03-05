from django.db import models
from faker import Faker
from .validators import validate_start_date


class Group(models.Model):
    title = models.CharField(
        max_length=50
    )
    start_date = models.DateField(validators=[validate_start_date])
    description = models.TextField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        __tablename__ = 'groups'

    def __str__(self):
        return f'Group name:{self.name}'

    @classmethod
    def generate_data(cls, count: int):
        faker = Faker()
        for _ in range(count):
            group = cls()
            group.title = faker.word().capitalize()
            group.start_date = faker.date_between(start_date='+0y', end_date='+5y')
            group.description = faker.text()
            group.save()
