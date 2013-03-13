from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from orderable.models import Orderable

from media_app.models import Image

class Axis(Orderable):
    name = models.CharField(max_length=255, verbose_name=_("Name (NL)"))
    name_en = models.CharField(max_length=255, blank=True, verbose_name=_("Name (EN)"))
    name_fr = models.CharField(max_length=255, blank=True, verbose_name=_("Name (FR)"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this axis."))
    description = models.TextField(verbose_name=_("Description (NL)"))
    description_en = models.TextField(blank=True, verbose_name=_("Description (FR)"))
    description_fr = models.TextField(blank=True, verbose_name=_("Description (EN)"))
    pictogram = models.CharField(max_length="20", verbose_name=_("Drawing (filename without extension)"))
    image_set = generic.GenericRelation(Image)
    
    def __unicode__(self):
        return self.name
