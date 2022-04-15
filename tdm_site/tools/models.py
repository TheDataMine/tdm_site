from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Tool(models.Model):
    """
    Model for a tool.
    """

    name = CharField(_("Name"), blank=True, max_length=255)
    description = models.TextField(_("Description"), blank=True)
    slug = models.SlugField(_("Slug"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for company's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("tools:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Override save method to generate slug.
        """
        if not self.slug:
            self.slug = slugify(self.keyword)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
