from django.db import models
from django.db.models import CharField, TextField, IntegerField, ForeignKey, ManyToManyField, BooleanField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Project(models.Model):
    """
    Model for a project.
    """
    project_pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = ForeignKey("companies.Company", on_delete=models.CASCADE, verbose_name=_("Company"))

    title = CharField(_('title'), max_length=100)
    slug = CharField(_('slug'), max_length=100, unique=True)
    summary = TextField(_('summary'), max_length=280)
    description = TextField(_('description'), max_length=1000)
    year = IntegerField(_('year'), blank=False)

    labtimes = ManyToManyField("classtimes.Labtime", verbose_name=_("labtimes"))
    lecturetimes = ManyToManyField("classtimes.Lecturetime", verbose_name=_("lecturetimes"))

    tools = ManyToManyField("tools.Tool", verbose_name=_("tools"))
    keywords = ManyToManyField("keywords.Keyword", verbose_name=_("keywords"))

    domain = ForeignKey("domains.Domain", verbose_name=_("domain"), on_delete=models.CASCADE)
    citizenship_status = ForeignKey("CitizenshipStatus", verbose_name=_("citizenship status"), on_delete=models.CASCADE)

    restricted = BooleanField(default=False)

    registration_status = BooleanField(default=False, verbose_name=_("Registration Status"))

    deafpods_bool = BooleanField(default=False, verbose_name=_("DEAFPODS"))



    def get_absolute_url(self):
        """Get url for company's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("projects:detail", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        """
        On save, check if slug already exists, if not, use the
        "slugified" version of the company name. Otherwise, don't
        touch it.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-updated_at"]


class CitizenshipStatus(models.Model):
    """
    Model for a citizenship status.
    """

    status = CharField(_('status'), max_length=100)
    slug = CharField(_('slug'), max_length=100, unique=True)
    description = TextField(_('description'), max_length=1000)


    def save(self, *args, **kwargs):
        """
        On save, check if slug already exists, if not, use the
        "slugified" version of the company name. Otherwise, don't
        touch it.
        """
        if not self.slug:
            self.slug = slugify(self.status)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "statuses"
