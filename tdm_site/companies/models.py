from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Company(models.Model):
    """
    Model for company.
    """

    name = CharField(_("Name of Company"), blank=True, max_length=255)
    slug = models.SlugField(null=False, default="")

    def get_absolute_url(self):
        """Get url for company's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("companies:detail", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        """
        On save, check if slug already exists, if not, use the
        "slugified" version of the company name. Otherwise, don't
        touch it.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "companies"