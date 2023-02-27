from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import students

DOMAINS = ('gmail.com', 'yahoo.com')


def validate_email_domain(value):
    # domains = ('gmail.com', 'yahoo.com')  # email_name@domain.com --> ['email.name', 'domain.com']
    domain = value.split('@')[-1]
    # if domain not in domains:

    if domain not in DOMAINS:
        raise ValidationError(f'Emails domain "{domain}" is not correct.')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'Emails domain "{domain}" is invalid.')


'''class ValidateEmailDomain:
    def __init__(self, *domains: tuple):
        self.domains = tuple(domains) if domains else DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[1]
        if domain not in self.domains:
            raise ValidationError(f'This email domain {domain} is not correct.')'''


def validate_email_unique(value: str):
    from .models import Student
    emails = [email['email'] for email in Student.objects.values('email').order_by('email')]

    if value in emails:
        raise ValidationError(f'Email: {value} is not unique.')
