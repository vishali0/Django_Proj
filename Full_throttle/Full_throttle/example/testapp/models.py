
from django.contrib.auth.models import AbstractUser
from activity_models.models import UserMixin


class User(AbstractUser, UserMixin):
    class Meta:
        verbose_name = 'user'


def make_extra_data(request, response):
    return str(request.META)