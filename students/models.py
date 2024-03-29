import datetime
import random
from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.models import PersonModel
from core.validators import validate_email_domain
from core.validators import ValidateEmailDomain
from core.validators import validate_email_unique
from groups.models import Group
from random import choice


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        if self.group:
            return f'{self.first_name} {self.last_name}({self.group.title})'
        else:
            return f'{self.first_name} {self.last_name}( )'




    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        student.save()
