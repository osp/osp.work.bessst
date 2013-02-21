from django.db import models
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
from axis.models import Axis
from django.contrib.contenttypes import generic
from media_app.models import Image

class Event(models.Model):
    published = models.BooleanField(_("Published"), default=False)
    title = models.CharField(max_length=255, verbose_name=_("Title (NL)"))
    title_fr = models.CharField(max_length=255, verbose_name=_("Title (FR)"), blank=True)
    title_en = models.CharField(max_length=255, verbose_name=_("Title (EN)"), blank=True)
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    project = models.ForeignKey(Project, verbose_name=_("Related project"))
    #axis = models.ForeignKey(Axis, verbose_name=_("Axis")) # only if there's no related project
    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"))
    summary = models.TextField(_("Summary (NL)"), blank=True)
    summary_fr = models.TextField(_("Summary (FR)"), blank=True)
    summary_en = models.TextField(_("Summary (EN)"), blank=True)
    description = models.TextField(_("Description (NL)"), blank=True)
    description_fr = models.TextField(_("Description (FR)"), blank=True)
    description_en = models.TextField(_("Description (EN)"), blank=True)

    location = models.CharField(max_length=80, verbose_name=_("Location (NL)"), null=True)
    location_en = models.CharField(max_length=80, verbose_name=_("Location (EN)"), null=True)
    location_fr = models.CharField(max_length=80, verbose_name=_("Location (FR)"), null=True)

    image_set = generic.GenericRelation(Image)

    @models.permalink
    def get_absolute_url(self):
        return ('event-detail', (), {'slug': str(self.slug)})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-start_date', 'project', 'title']
