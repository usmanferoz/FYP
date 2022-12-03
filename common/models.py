from django.db import models
from django.db.models import TextChoices


# Create your models here.


class StatusChoices(TextChoices):
    ACTIVE = 1, "active"
    DELETED = 2, "deleted"


class LogsMixin(models.Model):
    status = models.CharField(max_length=250, null=True, blank=True, choices=StatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

