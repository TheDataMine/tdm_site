from django.db import models
from django.db.models import CharField, TimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Labtime(models.Model):
    """
    Model for labtime.
    """

    days = models.ManyToManyField("days.Day", verbose_name=_("days"))
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{' & '.join([d.name for d in self.days.all()])}: {self.start_time} - {self.end_time}"


class Lecturetime(models.Model):
    """
    Model for lecturetime.
    """

    days = models.ManyToManyField("days.Day", verbose_name=_("days"))
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{' & '.join([d.name for d in self.days.all()])}: {self.start_time} - {self.end_time}"