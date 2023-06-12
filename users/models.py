from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from base.models import BaseModel
import uuid

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User Model"""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    uuid = models.UUIDField(null=True, blank=True, unique=True, default=uuid.uuid4)

    username = models.CharField(
        ("username"),
        max_length=10,
        null=False,
        blank=True,
        unique=True,
        db_index=True,
        db_column="username",
    )

    name = models.CharField(("name"), max_length=50, blank=True, db_index=True)

    role_title = models.CharField(("Role"), max_length=100, blank=True)
    dept = models.CharField(("dept"), max_length=50, blank=True, db_index=True)
    location = models.CharField(("location"), max_length=50, blank=True, db_index=True)
    employee_no = models.CharField(
        ("employee number"), max_length=50, blank=True, db_index=True
    )

