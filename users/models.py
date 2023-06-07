
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
    REQUIRED_FIELDS = ["first_name"]
    ROLE_CHOICES = (('1', "Role1"), ('2', "Role2"))

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

    first_name = models.CharField(
        ("first name"), max_length=50, blank=True, db_index=True
    )
    middle_name = models.CharField(
        ("middle name"), max_length=50, blank=True, db_index=True
    )
    last_name = models.CharField(
        ("last name"), max_length=50, blank=True, db_index=True
    )

    role_title = models.CharField(
        ("Role"), max_length=100, choices=ROLE_CHOICES
    )
    dept = models.CharField(
        ("dept"), max_length=50, blank=True, db_index=True
    )
    location = models.CharField(
        ("location"), max_length=50, blank=True, db_index=True
    )
    employee_no = models.CharField(
        ("employee number"), max_length=50, blank=True, db_index=True
    )
    is_active = models.BooleanField(("active"), default=True)
    is_staff = models.BooleanField(("staff status"), default=False)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("updated_at"), auto_now=True, auto_now_add=False)
