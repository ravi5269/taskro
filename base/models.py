from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("created_at"), auto_now=True, auto_now_add=False)
