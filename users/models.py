from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import YankiUserManager


class User(AbstractUser):
    """Base user model with changed USERNAME_FIELD to email."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(_('email address'), unique=True, db_index=True)

    objects = YankiUserManager()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
