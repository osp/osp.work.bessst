from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from media_app.models import Image

class Axis(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    slug = models.SlugField(_("Slug"), unique=False, help_text=_("Unique identifier. Allows a constant targeting of this axis."))
    description = models.TextField(verbose_name=_("Description"))
    pictogram = models.CharField(max_length="20", verbose_name=_("Drawing (filename without extension)"))
    image_set = generic.GenericRelation(Image)
    
    def __unicode__(self):
        return self.name
