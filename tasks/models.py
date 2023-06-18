from django.db import models
from base.models import BaseModel
from users.models import uuid
from users.models import User


# Create your models here


class SubTask(BaseModel):
    STATUS_CHOICE = (
        ("1", "todo"),
        ("2", "in_progress"),
        ("3", "review"),
        ("4", "completed"),
        ("5", "cancel"),
    )

    name = models.CharField(("NAME"), max_length=100)
    description = models.CharField(("DESCRIPTION"), max_length=100)
    assigned = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(("STATUS"), choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return self.name


class Task(BaseModel):
    name = models.CharField(("NAME"), max_length=100)
    description = models.CharField(("DESCRIPTION"), max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    subtask = models.ManyToManyField(SubTask)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
