from django.db import models
from django.db.models import CharField, TimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Day(models.Model):
    """
    Model for day.
    """

    name = CharField(_("Day of the week"), blank=True, max_length=255)

    def __str__(self):
        return self.name
