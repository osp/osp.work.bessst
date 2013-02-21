from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from people.models import People
from django.contrib.contenttypes import generic
from media_app.models import Image

from random import randint

class Project(models.Model):
    published = models.BooleanField(_("Published"), default=False)
    archived = models.BooleanField(_("Archived"), default=False)

    title = models.CharField(max_length=255, verbose_name=_("Title (NL)"))
    title_en = models.CharField(max_length=255, verbose_name=_("Title (EN)"), blank=True)
    title_fr = models.CharField(max_length=255, verbose_name=_("Title (FR)"), blank=True)

    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle (NL)"), blank=True)
    subtitle_en = models.CharField(max_length=255, verbose_name=_("Subtitle (EN)"), blank=True)
    subtitle_fr = models.CharField(max_length=255, verbose_name=_("Subtitle (FR)"), blank=True)

    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this project."))
    producers = models.ManyToManyField(People, verbose_name=_("Partners"), related_name="producer_set")
    link = models.URLField(_("Link URL"), null=True, blank=True)

    location = models.CharField(max_length=80, verbose_name=_("Location (NL)"), null=True)
    location_en = models.CharField(max_length=80, verbose_name=_("Location (EN)"), blank=True, null=True)
    location_fr = models.CharField(max_length=80, verbose_name=_("Location (FR)"), blank=True, null=True)

    axis = models.ForeignKey(Axis, verbose_name=_("Axis"))

    summary = models.TextField(_("Summary (NL)"), blank=True)
    summary_en = models.TextField(_("Summary (EN)"), blank=True)
    summary_fr = models.TextField(_("Summary (FR)"), blank=True)

    description = models.TextField(_("Description (NL)"))
    description_en = models.TextField(_("Description (EN)"), blank=True)
    description_fr = models.TextField(_("Description (FR)"), blank=True)

    start_date = models.DateField(_("Start date"), blank=True, null=True)
    end_date = models.DateField(_("End date"), blank=True, null=True)
    image_set = generic.GenericRelation(Image)

#    @property
    def size_x(self):
        return randint(4, 14)
    
#    @property
    def size_y(self):
        return randint(2, 7)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', (), {'slug': str(self.slug)})
    
    class Meta:
        ordering = ["-id"]
        
