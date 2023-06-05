
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from base.models import BaseModel
import uuid


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Custom User Model"""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name"]
    ROLE_CHOICES = ((1, "Role1"), (2, "Role2"))

    uuid = models.UUIDField(null=True, blank=True, unique=True, default=uuid.uuid4)

    username = models.CharField(
        _("username"),
        max_length=10,
        null=False,
        blank=True,
        unique=True,
        db_index=True,
        db_column="username",
    )

    first_name = models.CharField(
        _("first name"), max_length=50, blank=True, db_index=True
    )
    middle_name = models.CharField(
        _("middle name"), max_length=50, blank=True, db_index=True
    )
    last_name = models.CharField(
        _("last name"), max_length=50, blank=True, db_index=True
    )

    role_title = models.CharField(
        _("organization"), max_length=100, choices=ROLE_CHOICES
    )
    dept = models.CharField(
        _("dept"), max_length=50, blank=True, db_index=True
    )
    location = models.CharField(
        _("location"), max_length=50, blank=True, db_index=True
    )
    employee_no = models.CharField(
        _("employee number"), max_length=50, blank=True, db_index=True
    )
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_verified = models.BooleanField(default=False)
